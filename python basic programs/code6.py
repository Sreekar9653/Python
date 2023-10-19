a=""
while(a!="stop"):
    e=""
    a=input("Enter terms separating with space ").split()
    for i in range(len(a)):e=e+a[i]
    print(int(e))
    a=input("Enter word, enter stop if done ")
          
