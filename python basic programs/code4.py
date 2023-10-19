a,p=input("Enter word, enter stop if done"),0
while(a!="stop"):
    for i in range(len(a)):a=a[:i]+"@"+a[i+1:] if(a[i]==a[0] and i!=0) else a
    print(a)
    a=input("Enter word, enter stop if done")
          
