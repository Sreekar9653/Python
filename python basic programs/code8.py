t=0
def take(a):
    global t
    b=[]
    s=int(input("Enter rows for matrix"+str(a))) if(a==1) else t
    t=int(input("Enter cols for matrix"+str(a)))
    for i in range(s):
        b.append([])
        for j in range(t):
            b[-1].append(int(input("Enter value for a{}{} ".format(i+1,j+1))))
    print("matrix{} is".format(a),b)
    return b
while(input("Enter any number to continue, -1 to stop ")!="-1"):
    g,h=take(1),take(2)
    k=[]
    for i in range(len(g)):
        k.append([])
        for j in range(len(h[0])): #2x3*3x4=3x4
            l=0
            for p in range(len(g[0])):
                l=l+g[i][p]*h[p][j]
            k[-1].append(l)
    print(k)
