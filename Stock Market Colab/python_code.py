"""---
# Importing libraries
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import time
from dateutil.relativedelta import relativedelta
from threading import Thread
from datetime import datetime
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
from pandas.plotting import register_matplotlib_converters
from keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import MinMaxScaler
from pandas_datareader import data as pdr
yf.pdr_override()
from datetime import datetime
import pandas as pd

"""---
#Collecting latest stock market dataset
"""

stocks={'AAPL':[], 'GOOG':[], 'MSFT':[], 'AMZN':[]}
tstocks={'AAPL':[], 'GOOG':[], 'MSFT':[], 'AMZN':[]}
stocklist=[]
sdate,edate=0,0
def data_collect(tech_list,start,end,tr="Train"):
  #tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
  global stocks,tstocks
  #end = datetime.now()
  #start = datetime(end.year - 1, end.month, end.day)
  for stock in tech_list:
      if(tr=="Train") : stocks[stock] = yf.download(stock, start, end)
      else : tstocks[stock] = yf.download(stock, start, end)
  return "Downloading data..."

"""

---

#Including Date column as index"""

def date_include(tr="train"):
  global stocks,stocklist,tstocks
  for i in range(len(stocklist)):
    if(tr=="train"):
      stocks[stocklist[i]].to_csv(os.path.join(app.root_path, 'static/'+stocklist[i]+'_'+tr+'_data.csv'))                 # Date values act as row index
      stocks[stocklist[i]]=pd.read_csv(os.path.join(app.root_path, 'static/'+stocklist[i]+'_'+tr+'_data.csv'))            # Now Date is a column
    else:
      tstocks[stocklist[i]].to_csv(os.path.join(app.root_path, 'static/'+stocklist[i]+'_'+tr+'_data.csv'))                # Date values act as row index
      tstocks[stocklist[i]]=pd.read_csv(os.path.join(app.root_path, 'static/'+stocklist[i]+'_'+tr+'_data.csv'))           # Now Date is a column
  return "Preparing training dataset..."

"""

---

#Preparing training_set for Open column"""

def prepset():
  global training_set, scaler
  training_set=[]
  for i in range(len(stocklist)):
    training_set.append(stocks[stocklist[i]].iloc[:,1:2].values)
  return "Normalizing the data..."

"""

---

#Normalizing data for greater convergence"""

def normal():
  global scaler
  scaler=[]
  for i in range(len(training_set)):
    scaler.append(MinMaxScaler(feature_range=(0,1)))
    training_set[i]=scaler[-1].fit_transform(np.array(training_set[i]))
  return "Preparing inputs..."

"""

---

#Preparing array of inputs"""

def prepinp():
  global X_train,y_train
  X_train,y_train=[],[]
  def prth(num):
    X = []
    y = []
    for i in range(60,len(stocks[stocklist[num]])):
      X.append(training_set[num][i-60:i, 0])
      y.append(training_set[num][i, 0])
    X_train.insert(num,np.array(X))
    y_train.insert(num,np.array(y))
  for i in range(len(stocklist)):
    t=Thread(target=prth,args=[i])
    t.start()
  time.sleep(15)
  return "Reshaping inputs..."

"""---

#Reshaping inputs to LSTM format(3d)
"""

def rshape():
  global X_train
  for i in range(len(stocklist)):
    X_train[i] = np.reshape(X_train[i], (X_train[i].shape[0], X_train[i].shape[1], 1))
  return "Building model..."

"""---
#Building model
"""

def modebui():
  global X_train,reg
  reg=[]
  for i in range(len(stocklist)):
    regressor = Sequential()
    regressor.add(LSTM(units = 50, return_sequences= True, input_shape = (X_train[i].shape[1], 1)))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units = 50, return_sequences= True))
    regressor.add(Dropout (0.2))
    regressor.add(LSTM(units = 50, return_sequences= True))
    regressor.add(Dropout (0.2))
    regressor.add(LSTM(units = 50))
    regressor.add(Dropout (0.2))
    regressor.add(Dense (units=1))
    reg.append(regressor)
  return "Fitting model..."

"""---
#Fitting model
"""

def fitrmode():
  global X_train,y_train,reg
  def fitm(num):
    reg[num].compile(optimizer = 'adam', loss = 'mean_squared_error')
    reg[num].fit(X_train[num], y_train[num], epochs=20, batch_size=64)
  for i in range(len(stocklist)):
    t=Thread(target=fitm,args=[i])
    t.start()
  time.sleep(90)
  return "Preparing testing data..."

"""---
#Preparing testing data
"""

def preptest():
  global edate,stocklist,tstocks,actual_stock_price
  data_collect(stocklist,edate-relativedelta(months=1),edate,"Test")
  date_include("test")
  actual_stock_price=[]
  for i in range(len(stocklist)):
    actual_stock_price.append(tstocks[stocklist[i]].iloc[:,1:2].values)
  return "Preparing testing inputs..."

"""---
#Preparing testing inputs
"""

def ptestinp():
  global stocks,stocklist,tstocks,X_test,scaler
  X_test=[]
  def testthread(num):
    dataset_total = pd.concat((stocks[stocklist[num]]['Open'], tstocks[stocklist[num]]['Open']), axis= 0)
    inputs = dataset_total[len(dataset_total)- len(tstocks[stocklist[num]])-60:].values
    inputs = inputs.reshape(-1,1)
    inputs = scaler[num].transform(inputs)
    X= []
    for i in range(60,60+len(tstocks[stocklist[num]])):
      X.append(inputs [i-60:i, 0].tolist())
    X = np.array(X)
    X_test.insert(num,np.reshape(X, (X.shape[0], X.shape[1], 1)))
  for i in range(len(stocklist)):
    t=Thread(target=testthread,args=[i])
    t.start()
  time.sleep(15)
  return "Predicting..."

"""---
#Prediction
"""

def pred():
  global predicted_stock_price,reg,scaler
  predicted_stock_price=[]
  for i in range(len(stocklist)):
    p=reg[i].predict(X_test[i])
    predicted_stock_price.append(scaler[i].inverse_transform(p))

"""---
#Graphs
"""

def grph():
  pred()
  for i in range(len(stocklist)):
    plt.plot(actual_stock_price[i], color = 'red', label = 'Actual '+stocklist[i]+' Stock Price')
    plt.plot(predicted_stock_price[i], color = 'blue', label = 'Predicted '+stocklist[i]+' Stock Price')
    plt.xlabel('Time')
    plt.ylabel(stocklist[i]+' Stock Price')
    plt.legend()
    plt.show()

"""---
#Installing ngrok for flask in colab
"""

pip install -q flask-ngrok

"""---
#Getting ngrok running files from web
wget - **web get**<br>
tar - **tape archieve** for extracting archieved files <br>
authtoken sets a **secret key** for avoiding entry to hackers
"""

!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz
!tar -xvf /content/ngrok-stable-linux-amd64.tgz
!./ngrok authtoken 23H0IY10fqeKMIW7kG05JhKZMae_3Zabr2iqkU9AUcZ7CrRTP

"""--
#Flask libraries
"""

# import Flask from flask module
from flask import Flask,render_template, redirect, url_for, request

# import run_with_ngrok from flask_ngrok to run the app using ngrok
from flask_ngrok import run_with_ngrok

#setting app as Flask app
app = Flask(__name__)
run_with_ngrok(app)

"""---
#Exception handling
"""

import traceback

@app.errorhandler(Exception)
def handle_exception(e):
    #Use for stack trace
    return traceback.format_exc()

"""---
#Flask Main Thread
"""

@app.route("/",methods=['GET','POST'])
def py3():
  return render_template("Homep.html")

"""---
#Function to handle function calls
"""

def funs(n):
    global sd
    print("Step",n,"-",datetime.now())
    if(n==0):sd="Collecting resources..."
    elif(n==1):sd=data_collect(stocklist,sdate,edate-relativedelta(months=1))
    elif(n==2): sd=date_include()
    elif(n==3): sd=prepset()
    elif(n==4): sd=normal()
    elif(n==5): sd=prepinp()
    elif(n==6): sd=rshape()
    elif(n==7): sd=modebui()
    elif(n==8): sd=fitrmode()
    elif(n==9): sd=preptest()
    elif(n==10): sd=ptestinp()
    print(sd)

"""---
#Form where user can fill details about prediction
"""

@app.route("/pyfl",methods=['GET','POST'])
def pyfl():
  global tc
  tc=-1
  return render_template("selec.html")

"""---
#Final Result page
"""

@app.route("/progress",methods=['GET','POST'])
def over():
  grph()
  return redirect(url_for('py3'))

"""#Loading page"""

@app.route("/py1",methods=['GET','POST'])
def py2():
  global stocklist,sdate,edate,tc,sd
  if(tc==-1):
    edate=datetime.strptime(request.form.get("d1"),"%Y-%m-%d")
    stocklist=request.form.getlist("r1")
    s=request.form.get("d2").split()
    d=relativedelta(months=int(s[0])) if(s[1]=="months") else relativedelta(years=int(s[0]))
    sdate=edate-d
  tc=tc+1
  if(tc==11):return redirect(url_for("over"));
  funs(tc)
  return render_template("trial.html",pgstat=sd,width=tc*10,tc=tc)

"""---
# Running flask
"""

if __name__ == "__main__":app.run()