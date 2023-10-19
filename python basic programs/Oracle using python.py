import cx_Oracle as c
con=c.connect("C##MCA24/MCA24@orcl")
table=input("enter table to create")
cursor=con.cursor()
cursor.execute("create table "+table+"(eid integer primary key, name varchar2(30),salary number(10,2))")
print("Table created")
import cx_Oracle as c
con=c.connect("C##MCA24/MCA24@orcl")
cursor=con.cursor()
    def insert(a1="w",a2=2,a3="s"):
        global cursor,table
        while(not a1.isdigit()):a1=input("enter value for id")
        while(not a2.isalpha()):a2=input("enter value for name")
        while(not a3.isdigit()):a3=int(input("enter value for salary")) 
        cursor.execute("insert into "+table+" values(:1,:2,:3)",(a1,a2,a3))
        return "Record inserted"
    def fin(abc=""):
        global cursor,table
        while(type(abc)!=int): print("Please enter integer")
        if(list(cursor.execute("select * from "+table+" where eid="+abc))!=[]):
            s=list(cursor.execute("select * from "+table+" where eid="+abc))
            return s
        else:return "Id doesnt exist"
    def updat(abc=""):
        global cursor,table
        while(type(abc)!=int): print("Please enter integer")
        if(list(cursor.execute("select * from "+table+" where eid="+abc))!=[]):
            s=list(cursor.execute("select * from "+table+" where eid="+abc))
            return s
        else:return "Id doesnt exist"
    def delete(abc=""):
        global cursor,table
        while(type(abc)!=int): print("Please enter integer")
        if(list(cursor.execute("delete from "+table+" where eid="+abc))!=[]):
            s=list(cursor.execute("select * from "+table+" where eid="+abc))
            return s
        else:return "Id doesnt exist"
a="z"
while(input("enter 1 to continue"=="1")):
    s="to create press 1, to insert press 2, to select press 3,to update press 4, to delete press 5"
    while(ord(a)<49 or ord(a)>53): a=input(s)
    ad={"1":create_table,"2":insert,"3":fin,"4":updat,"5":delete}
    ad[int(a)]()
con.commit()
