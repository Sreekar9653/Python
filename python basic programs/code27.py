ch="y"
while ch=="y":
    from abc import ABC, abstractmethod
    class shape(ABC):
        @abstractmethod
        def area(self):
            raise NotImplementedError()
        def perimeter(self):
            pass
        def display():
            pass

    class rectangle(shape):
        def __init__(self,l,b):
            self.l=l
            self.br=b
            self.a=0
            self.b=0
        def area(self):
            self.a=self.l*self.br
        def perimeter(self):
            self.b=2*(self.l+self.br)
        def display(self):
            self.area()
            self.perimeter()
            print("Area of rectangle is ",self.a)
            print("Perimeter of rectangle is ",self.b)
            
    class triangle(shape):
        def __init__(self,b,h,s,s2):
            self.l=h
            self.br=b
            self.s1=s2
            self.s=s
            self.a=0
            self.b=0
        def area(self):
            self.a=(self.l*self.br)/2
        def perimeter(self):
            self.b=2*(self.s+self.br+self.s1)
        def display(self):
            self.area()
            self.perimeter()
            print("Area of triangle is ",self.a)
            print("Perimeter of triangle is ",self.b)

    class circle(shape):
        def __init__(self,r):
            self.l=r
            self.a=0
            self.b=0
        def area(self):
            self.a=(22/7)*self.l**self.l
        def perimeter(self):
            self.b=(44/7)*self.l
        def display(self):
            self.area()
            self.perimeter()
            print("Area of circle is ",self.a)
            print("Perimeter of circle is ",self.b)

    class rhombus(shape):
        def __init__(self,l,b,a):
            self.l=l
            self.br=b
            self.a=a
            self.b=0
        def area(self):
            self.ar=self.l*self.br/2
        def perimeter(self):
            self.b=4*self.a
        def display(self):
            self.area()
            self.perimeter()
            print("Area of rhombus is ",self.ar)
            print("Perimeter of rhombus is ",self.b)

    rectangle(3,4).display()
    triangle(3,4,2,5).display()
    circle(4).display()
    rhombus(3,4,3).display()
    ch=input("Enter y to continue")
    
