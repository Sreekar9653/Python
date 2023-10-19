with open(input("Enter file ")) as f:
    i,n,p,q=[],[],[],[]
    for j in f:
        a,b,c,d=j[:-1].split(',') if(j[-1]=="\n") else j.split(',')
        i,n,p,q=[i+[a],n+[b],p+[int(c)],q+[d]]

    b=input("Enter item ")
    print(i[n.index(b)],b,p[n.index(b)],q[n.index(b)])

    k=p.index(sorted(p)[-1])
    print("\nCostliest item is [{},{},{},{}]".format(i[k],n[k],p[k],q[k]))

    print("\nname\t\tprice")
    for t in range(len(n)):
        print("{}\t\t{}".format(n[t],p[t]))
    
