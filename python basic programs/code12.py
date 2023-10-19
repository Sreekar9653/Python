s=input("Enter a string ").split()
while(s):
    s.sort()
    d=dict()
    for i in range(len(s)):
        d[s[i][0]]=d[s[i][0]]+[s[i]] if(s[i][0] in d.keys()) else [s[i]]
    print(d)
    s=input("Enter a string ").split()
    
        
        
