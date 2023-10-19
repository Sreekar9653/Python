a=""
while(a!="stop"):
    b=int(input("Enter multplier"))
    a=input("Enter terms separating with space ").split()*b
    for i in range(len(a)):a[i]=a[i]+str(i//(len(a)//b) +1)
    print(a)
    a=input("Enter word, enter stop if done ")
          
