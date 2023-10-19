a=input("Enter a string")
d={"{":0,"[":0,"(":0}
while a:
    for i in a:
        if(i=='{' or i=='(' or i=='['):
            d[i]= d[i]+1
        elif(i=='}' or i==')' or i==']'):
            e='{' if i=='}' else '(' if(i==')') else '['
            d[e]=d[e]-1
    print(d['{']==0 and d['(']==0 and d['[']==0)
    a=input("Enter a string")
