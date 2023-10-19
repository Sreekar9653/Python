# Program to
# add ly if last three characters of string are "ing"
# add ing if string length is more than 2
# return the string if length is less than 3

a=input("Enter word, enter stop if done")
while(a!="stop"):
    print(a if(len(a)<3) else a+"ly" if(a[-3:]=="ing") else a+"ing")
    a=input("Enter word, enter stop if done")
          
