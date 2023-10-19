import re
a=input("To continue enter string or leave empty ")
while(a):
    print("".join(re.findall("\W+|\w+",a)[::-1]))
    a=input("To continue enter string or leave empty ")
