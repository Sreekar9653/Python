class Power:
    def power(self,x,n):
        return "{}^{}={}".format(x,n,pow(x,n))
print(Power.power(2,3))
