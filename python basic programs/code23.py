class getprint:
    string=''
    def get_string(self):
        self.string=input("Enter a string")
    def print_string(self):
        print("Your string is "+self.string)
g=getprint()
while(input("Enter 1 to continue ")=='1'):
    g.get_string()
    g.print_string()
