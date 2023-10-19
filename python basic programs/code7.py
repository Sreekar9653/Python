n="y"
while(n.casefold()!="n"):
    s,t=int(input("enter no of rows ")),int(input("enter no of cols "))
    e=[]
    for i in range(-1,s*t):a=[] if(i==-1) else a+[[input("Enter value for a{}{} : ".format(i//t +1, i%t +1))]] if(i%t==0) else a[:-1]+[a[-1]+[input("Enter value for a{}{} : ".format(i//t +1, i%t +1))]]
    print(a)
    for i in range(t): 
        e.append([])   
        for j in range(s): 
            e[-1].append(a[j][i])
    print(e)                                   
    n=input("Do you want to continue y/n ").strip()
