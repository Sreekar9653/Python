import operator as op
import re
class IllegalNumberOfArguments(Exception):
    pass
class InvalidOperatorException(Exception):
    pass
class NegativeResultException(Exception):
    pass
operators=[]
def operate(a=['+','-','*','/','//','%','**'][::-1]):
    for i in a:
        if(i in operators):return [i,operators.index(i)]
d={'+':op.add,"-":op.sub,'*':op.mul,'/':op.truediv,'//':op.floordiv,'%':op.mod,'**':op.pow}
def accept(operand):
    if(not operand):return ""
    global operators
    try:
        if(len(operand)<3):raise IllegalNumberOfArguments()
        while(len(operators)<2):
            operator=input("Enter operator"+str(len(operators)+1)+" from '+','-','*','/','//','%','**' ")
            if(operator in ['+','-','*','/','//','%','**']):operators.append(operator)
            else:raise InvalidOperatorException()
        if(len(operand)==3):
            while(operators):
                cu=operate()
                operand[cu[1]:cu[1]+2]=[d[cu[0]](operand[cu[1]],operand[cu[1]+1])]
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

