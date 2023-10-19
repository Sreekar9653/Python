from os import system

def take_nos():
    try:a = int(input("Enter no from 1 to 22, 0 to stop "))
    except ValueError:
        print("Please enter integer!!!\n")
    else:
        if(a<0 or a>22):
            print("Please enter no from 0 to 21\n")
        else:return a
    return take_nos()

def p1():
    """Write a program to find the count of all occurrences of characters in a string"""
    a = input("Enter word, enter stop if done ")
    while(a!= "stop"):
        d = dict()
        for i in range(len(a)):
            if(a[i] not in a[:i]):d[a[i]] = a.count(a[i])
        print(d)
        a = input("Enter word, enter stop if done ")

def p2():
    """Write a program to print first and last two characters of a string"""
    a = input("Enter word, enter stop if done ")
    while(a!= "stop"):
        print(a if(len(a)<2) else a[:2]+a[-2:])
        a = input("Enter word, enter stop if done ")

def p3():
    """Write a program to add 'ly' if ending 3 characters are 'ing' else 'ing' if string has more than 2 characters else nothing"""
    a = input("Enter word, enter stop if done ")
    while(a!= "stop"):
        print(a if(len(a)<3) else a+"ly" if(a[-3:] =  = "ing") else a+"ing")
        a = input("Enter word, enter stop if done ")

def p4():
    """Write a program to change all occurences of first letter with a string """
    a = input("Enter word, enter stop if done ")  
    while(a!= "stop"):
        string = input("Enter a string to replace ")
        for i in range(len(a)):a = a[:i] + string + a[i+1:] if(a[i] =  = a[0] and i!= 0) else a
        print(a)
        a = input("Enter word, enter stop if done ")

def p5():
    """Write a program to add indices in given list(eg. [p,q] can give output as [[p1,q1],[p2,q2],[p3,q3],[p4,q4],[p5,q5]])"""
    a = ""
    while(a!= "stop"):
        b = int(input("Enter multplier "))
        a = input("Enter terms separating with space ").split()*b
        for i in range(len(a)):a[i] = a[i]+str(i//(len(a)//b) +1)
        print(a)
        a = input("Enter word, enter stop if done ")

def p6():
    """Write a program to join list of numbers into one integer"""
    a = ""
    while(input("Press 'Enter' to stop, any other key to continue ")):
        n = []
        for i in range(int(input("Enter no of values in list" ))):n+ = list(input("Enter value"+str(i+1)))
        try:print(int("".join(n)))
        except ValueError:
            print("Enter numbers only")
            return p6()

def p7():
    """Transpose of matrix"""
    n = "y"
    while(n.casefold()!= "n"):
        s,t = int(input("enter no of rows ")),int(input("enter no of cols "))
        e = []
        for i in range(-1,s*t):a = [] if(i =  = -1) else a+[[input("Enter value for a{}{} : ".format(i//t +1, i%t +1))]] if(i%t =  = 0) else a[:-1]+[a[-1]+[input("Enter value for a{}{} : ".format(i//t +1, i%t +1))]]
        print("Given matrix : ",a)
        for i in range(t): 
            e.append([])   
            for j in range(s): 
                e[-1].append(a[j][i])
        print("Transpose : ",e)                                   
        n = input("Do you want to continue y/n ").strip()

def p8():
    """Matrix Multiplication"""
    t = 0
    def take(a):
        global t
        b = []
        s = int(input("Enter rows for matrix"+str(a))) if(a =  = 1) else t
        t = int(input("Enter cols for matrix"+str(a)))
        for i in range(s):
            b.append([])
            for j in range(t):
                b[-1].append(int(input("Enter value for a{}{} ".format(i+1,j+1))))
        print("matrix{} is".format(a),b)
        return b
    while(input("Enter any number to continue, -1 to stop ")!= "-1"):
        g,h = take(1),take(2)
        k = []
        for i in range(len(g)):
            k.append([])
            for j in range(len(h[0])): #2x3*3x4 = 3x4
                l = 0
                for p in range(len(g[0])):
                    l = l+g[i][p]*h[p][j]
                k[-1].append(l)
        print(k)
        
def p9():
    """Well bracketed"""
    a = input("Enter a string")
    d = {"{":0,"[":0,"(":0}
    while a:
        for i in a:
            if(i =  = '{' or i =  = '(' or i =  = '['):
                d[i] =  d[i]+1
            elif(i =  = '}' or i =  = ')' or i =  = ']'):
                e = '{' if i =  = '}' else '(' if(i =  = ')') else '['
                d[e] = d[e]-1
        print(d['{'] =  = 0 and d['('] =  = 0 and d['['] =  = 0)
        a = input("Enter a string")

def p10():
    """List rotation"""
    l = list(input("Enter a list as 12345"))
    k = int(input("Enter a positive integer"))
    print(l if(k<0) else l[-k:]+l[:-k])

def p11():
    """Check whether string is in ascending or not"""
    a = input("Enter a string")
    def ascending(l):
        for i in range(len(l)-1):
            if(ord(l[i])>ord(l[i+1])):
                return ["False","Not ascending"]
        return ["True","Ascending"]
    print("{}\n{}".format(ascending(a)[0],ascending(a)[1]))

def p12():
    """Write a program to divide words of a string using the first character of word"""
    s = input("Enter a string ").split()
    while(s):
        s.sort()
        d = dict()
        for i in range(len(s)):
            d[s[i][0].lower()] = d.get(s[i][0].lower(),[])+[s[i]]
        print(d)
        s = input("Enter a string ").split()

def p13():
    """File handling
     . Search an element
     . Find the costliest item
     . Show only name and prices of all items"""
    with open(input("Enter file ")) as f:
        i,n,p,q = [],[],[],[]
        for j in f:
            a,b,c,d = j[:-1].split(',') if(j[-1] =  = "\n") else j.split(',')
            i,n,p,q = [i+[a],n+[b],p+[int(c)],q+[d]]

        b = input("Enter item ")
        print(i[n.index(b)],b,p[n.index(b)],q[n.index(b)])

        k = p.index(sorted(p)[-1])
        print("\nCostliest item is [{},{},{},{}]".format(i[k],n[k],p[k],q[k]))

        print("\nname\t\tprice")
        for t in range(len(n)):
            print("{}\t\t{}".format(n[t],p[t]))

def p14():
    '''File with Max Size'''
    import glob
    import os
    dir_name  =  'D:/'
    list_of_files  =  filter( os.path.isfile, glob.glob(dir_name + '*') )
    max_file  =  max( list_of_files, key  =   lambda x: os.stat(x).st_size)
    print('Max File: ', max_file)
    print('Max File size in bytes: ', os.stat(max_file).st_size)

def p15():
    '''All files in a directory'''
    import glob
    import os
    dir_name  =  'D:/'
    list_of_files  =  filter( os.path.isfile, glob.glob(  dir_name + '*') )
    print(glob.glob(dir_name +"*"))

def p16():
    '''Testing
     . No of Arguments is less than 3
     . Character is an arithmetic operator
     . Solution of a operation is negative'''
    import operator as op
    import re
    class IllegalNumberOfArguments(Exception):
        pass
    class InvalidOperatorException(Exception):
        pass
    class NegativeResultException(Exception):
        pass
    operators = []
    def operate(a = ['+','-','*','/','//','%','**'][::-1]):
        for i in a:
            if(i in operators):return [i,operators.index(i)]
    d = {'+':op.add,"-":op.sub,'*':op.mul,'/':op.truediv,'//':op.floordiv,'%':op.mod,'**':op.pow}
    def accept(operand):
        if(not operand):return ""
        nonlocal operators
        try:
            if(len(operand)<3):raise IllegalNumberOfArguments()
            while(len(operators)<2):
                operator = input("Enter operator"+str(len(operators)+1)+" from '+','-','*','/','//','%','**' ")
                if(operator in ['+','-','*','/','//','%','**']):operators.append(operator)
                else:raise InvalidOperatorException()
            if(len(operand) =  = 3):
                while(operators):
                    cu = operate()
                    operand[cu[1]:cu[1]+2] = [d[cu[0]](operand[cu[1]],operand[cu[1]+1])]
                    operators.pop(cu[1])
                if(operand[0]<0):raise NegativeResultException
                else:print("Result is {}".format(operand[0]))
        except IllegalNumberOfArguments:print("Please enter three operands")
        except InvalidOperatorException:
            print("Arithmetic operator required")
            return accept(operand)
        except NegativeResultException:print("Result is negative({})".format(operand[0]))
        return accept(list(map(int,re.findall("\d+",input("Enter 3 nos separating with space as operands, Enter to exit ")))))
    print(accept(list(map(int,re.findall("\d+",input("Enter 3 nos separating with space as operands, Enter to exit "))))))

def p17():
    '''Check whether alphabet is first letter of a color in Rainbow'''
    class Color:
        def Display_Color(a):
            if(not a):return
            try:
                if(not(len(a) =  = 1 and a.isalpha())):raise TypeError("An Alphabet should be taken")
                elif(a.lower() in "vibgyor"):print({'v':'violet','i':'indigo','b':'blue','g':'green','y':'yellow','o':'orange','r':'red'}[a.lower()])
                else:raise ValueError("Not a color")
            except TypeError:print("Alphabet should be taken")
            except ValueError:print("Not a color")
            return Color.Display_Color(input("Enter an Alphabet, leave empty if done "))
    Color.Display_Color(input("Enter an Alphabet, leave empty if done "))

def p18():
    '''Check whether student name has only letters and 15< = age< = 21'''
    class AgeNotWithinRangeException(Exception):
        pass
    class NameNotValidException(Exception):
        pass
    class Student:
        def __init__(self,rno,name,age,cou):
            self.rollno,self.name,self.age,self.counter = rno,name,age,cou
        def check(self):
            try:
                if(not self.name.isalpha()):raise NameNotValidException("Name should have only alphabets")
                if(int(self.age)<15 or int(self.age)>21):
                    raise AgeNotWithinRangeException("Name should have only alphabets")
            except NameNotValidException: print("Name should have only alphabets")
            except AgeNotWithinRangeException:print("Please enter age within range")
            except:pass
            if(input("To continue enter y else any other key ").lower() =  = 'y'):
                c = Student(input("Enter rollno "),input("Enter name "),input("Enter age "),input("Enter course "))
                return c.check()
    c = Student(input("Enter rollno "),input("Enter name "),input("Enter age "),input("Enter course "))
    c.check()

def p19():
    '''Integer to roman'''
    def take_nos():
        try:a = int(input("Enter no from 1 to 3999, 0 to stop "))
        except ValueError:
            print("Please enter integer!!!\n")
        else:
            if(a<1 or a>3999):
                print("Please enter no from 1 to 3999\n")
            else:return a
        return take_nos()
    class Roman:
        def convert(a):
            l = [["I","V"],["X","L"],["C","D"],["M"]]
            while(a):
                first_digit = a//10**(len(str(a))-1)
                if(first_digit =  = 4):print(l[len(str(a))-1][0]+l[len(str(a))-1][1], end = "")
                elif(first_digit =  = 9):print(l[len(str(a))-1][0]+l[len(str(a))][0], end = "")
                elif(first_digit> = 5):print(l[len(str(a))-1][1]+l[len(str(a))-1][0]*(first_digit-5), end = "")
                elif(first_digit>0):print(l[len(str(a))-1][0]*(first_digit), end = "")
                a% = 10**(len(str(a))-1)
            print()
    Roman.convert(take_nos())

def p20():
    '''Find all terms having specified sum'''
    from itertools import combinations
    def take_nos(c):
        try:a = int(input(c))
        except ValueError:
            print("Please enter integer!!!\n")
        else:return a
        return take_nos(c)
    class Num:
        def Sum(l,s):
            a = []
            for i in range(2, len(l)):
                for j in combinations(l,i):
                    if(sum(j) =  = s):a.append(j)
            print(a if(a) else "No combination has sum"+str(s))
    a = []
    for i in range(take_nos("Enter no of values ")):a.append(take_nos("Enter value"+str(len(a)+1)+" "))
    Num.Sum(a,take_nos("Enter sum "))

def p21():
    '''Password matching
     . atleast 1 lowercase
     . atleast 1 uppercase
     . atleast 1 symbol [!@#$]
     . minimum 6
     . maximum 16 characters'''
    import re
    text = input("Enter password ,stop to stop")
    while(text.lower() =  = 'stop'):
        result = re.findall("(? = .*[a-z])(? = .*[A-Z])(? = .*[$&@#]).{6,16}",text)
        if(result):print("Password valid")
        else : print("Please match the required pattern")
        text = input("Enter password ")

def p22():
    '''Write a program to reverse strings by words'''
    import re
    a = input("To continue enter string or leave empty ")
    while(a):
        print("".join(re.findall("\W+|\w+",a)[::-1]))
        a = input("To continue enter string or leave empty ")

d = {
    1:p1, 2:p2, 3:p3, 4:p4, 5:p5, 6:p6, 7:p7, 8:p8, 9:p9,
    10:p10, 11:p11, 12:p12, 13:p13, 14:p14, 15:p15, 16:p16,
    17:p17, 18:p18, 19:p19, 20:p20, 21:p21, 22:p22
    }

while(1):
    system("clear")
    print("List of Programs:")
    for i in d:print(i,"-",d[i].__doc__)
    print()
    k = take_nos()
    if(k):
        print("\nProgram ",k," is running\n",d[k].__doc__)
        d[k]()
        print("Program ",k," is stopped\n")
    else:
        print("Compilation is over")
        break
