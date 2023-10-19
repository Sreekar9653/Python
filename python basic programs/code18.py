class AgeNotWithinRangeException(Exception):
    pass
class NameNotValidException(Exception):
    pass
class Student:
    def __init__(self,rno,name,age,cou):
        self.rollno,self.name,self.age,self.counter=rno,name,age,cou
    def check(self):
        try:
            if(not self.name.isalpha()):raise NameNotValidException("Name should have only alphabets")
            if(int(self.age)<15 or int(self.age)>21):
                raise AgeNotWithinRangeException("Name should have only alphabets")
        except NameNotValidException: print("Name should have only alphabets")
        except AgeNotWithinRangeException:print("Please enter age within range")
        except:pass
        if(input("To continue enter y else any other key ").lower()=='y'):
            c=Student(input("Enter rollno "),input("Enter name "),input("Enter age "),input("Enter course "))
            return c.check()
c=Student(input("Enter rollno "),input("Enter name "),input("Enter age "),input("Enter course "))
c.check()
