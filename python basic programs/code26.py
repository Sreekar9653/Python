class A:
    def __init__(self,name):
        self.a=name
    def __add__(self,b):
        return self.a+b.a;
class B:
    def __init__(self,a):
        self.a=a
print(A("Sachin")+B("Manoj"))
print(A(24)+B(27))
print(A(2.3)+B(2))
print(A(["2"])+B(["3"]))
    
