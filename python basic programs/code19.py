def take_nos():
    try:a=int(input("Enter no from 1 to 3999, 0 to stop "))
    except ValueError:
        print("Please enter integer!!!\n")
    else:
        if(a<1 or a>3999):
            print("Please enter no from 1 to 3999\n")
        else:return a
    return take_nos()
class Roman:
    def convert(a):
        l=[["I","V"],["X","L"],["C","D"],["M"]]
        while(a):
            first_digit=a//10**(len(str(a))-1)
            if(first_digit==4):print(l[len(str(a))-1][0]+l[len(str(a))-1][1], end="")
            elif(first_digit==9):print(l[len(str(a))-1][0]+l[len(str(a))][0], end="")
            elif(first_digit>=5):print(l[len(str(a))-1][1]+l[len(str(a))-1][0]*(first_digit-5), end="")
            elif(first_digit>0):print(l[len(str(a))-1][0]*(first_digit), end="")
            a%=10**(len(str(a))-1)
Roman.convert(take_nos())
