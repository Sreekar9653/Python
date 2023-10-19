l=list(input("Enter a list"))
k=int(input("Enter a positive integer"))
print(l if(k<0) else l[-k:]+l[:-k])
