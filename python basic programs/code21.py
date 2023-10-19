import re
while(input("Enter y to continue").lower()=='y'):
    text=input("Enter password ")
    result=re.findall("(?=.*[a-z])(?=.*[A-Z])(?=.*[$@#]).{6,16}",text)
    if(result):print("Password valid")
    else : print("Please match the required pattern")
