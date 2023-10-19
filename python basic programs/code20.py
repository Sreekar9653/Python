def take_nos(c):
    try:a=int(input(c))
    except ValueError:
        print("Please enter integer!!!\n")
    else:return a
    return take_nos(c)
class Num:
    def Sum(l,s):
        a=[]
        b=[]
        for i in range(len(l)):
            for j in range(len(l)):
                if(l[i]+l[j]==s and i!=j):
                    a.append([i,j])
                    b.append([l[i],l[j]])
        print("List of combinations with sum",l,"is",a,"\nRespective indices are",b)
a=[]
for i in range(take_nos("Enter no of values ")):a.append(take_nos("Enter value"+str(len(a)+1)+" "))
Num.Sum(a,take_nos("Enter sum "))
