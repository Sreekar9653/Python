from abc import ABC, abstractmethod
class Interest(ABC):
    @abstractmethod
    def simpleI(self,p,r,n):
        pass
    @abstractmethod
    def compoundI(self,p,r,n):
        pass

class simple(ABC):
    def simpleI(self,p,r,n):
        return (p*r*n)/100
    def compoundI(self,p,r,n):
        pass

class compound(ABC):
    def simpleI(self,p,r,n):
        pass
    def compoundI(self,p,r,n):
        c=(1+r/100)
        return p*pow(c,n)
s=simple()
print("Simple Interest is ", s.simpleI(25000,9.5,5))

s=compound()
print("Compound Interest is ", s.compoundI(25000,9.5,5))
