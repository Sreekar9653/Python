class A:
    b=0
    def __int__(self):
        print("This is class A")
class B:
    c=1
    def __init(self):
        print("This is Class B")
class C(A,B):
    def __init__(self,a):
        self.a=a
    def fun(self):
        print(A.b,B.c,self.a)
C(2).fun()
    
