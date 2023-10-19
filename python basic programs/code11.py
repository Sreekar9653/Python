a=input("Enter a string")
def find_ascii(l):
    for i in range(32,127):
        if(l==chr(i)):return i
def ascending(l):
    for i in range(len(l)-1):
        if(find_ascii(l[i])>find_ascii(l[i+1])):
            return ["False","Decending"]
    return ["True","Acending"]
print("{}\n{}".format(ascending(a)[0],ascending(a)[1]))
