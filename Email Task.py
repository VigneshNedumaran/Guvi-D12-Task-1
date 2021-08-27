import mysql.connector
import re
import random

mydb = mysql.connector.connect(host = "localhost",user="root",password="",database="mysql")
mycursor = mydb.cursor()


def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return(True)
    else:
        return(False)



def lower(username):
    lower = any(c.islower() for c in username)
    return lower

def upper(username):
    upper = any(c.isupper() for c in username)
    return upper

def digit(username):
    digit = any(c.isdigit() for c in  username)
    return digit
def getPassword(username):
    return(username)
def validate(username):
    lower = lower(username)
    upper = upper(username)
    digit = digit(username)

    length = len(username)

    report =  lower and upper and digit and length >= 5 and length <= 16

    if report:
        return True

    else:
        return False
def register(un,pw): 
    if check(un):
        if validate(pw):
            sql = "INSERT INTO register (Username,Password) VALUES (%s,%s)"
            val = (un,pw)   
            mycursor.execute(sql,val)
            mydb.commit()
            print("User Created Successfully")
        else:
            print("Password not met the criteria please retry")
    else:
        print("Please Enter a valid mail ID and continue")
def login(un,pw):
    sql = "Select * from  register where Username =  '"+ un+"'"
    try:
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        if myresult[2]==passwd:
            return True
        else:
            return False
    except:
        return False
def forgotpwd(un):
    sql = "Select * from  register where Username =  '"+ un+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    return myresult[2]
print("Welcome to My App")
while True:
    print("CHOICES")
    print("1.Register")
    print("2.Login")
    print("3.Exit")
    choice=int(input("Enter Your Choice: "))

    if choice == 1:
        
        print("Enter details to register")
        U=input("Enter Username: ")
        C = input("Enter Password : ")   
        register(U,C)  
    elif choice == 2:
        print("Enter Details.")
        uname=input("Enter Username: ")
        passwd=input("Enter Password: ")
        if login(uname,passwd):
            print("Logged in Sucessfully :) ")
        else:
            print("Please Enter a valid user name or password :(")
            print("1.Login Again")
            print("2.Forgot Password")
            print("3.Register")
            print("4.Exit")
            relog=int(input("Please enter Your Choice: "))
            if relog==1:
                uname=input("Enter Username: ")
                passwd=input("Enter Password: ")
                if login(uname,passwd):
                    print("Logged in Sucessfully :)")
                else:
                    print("You have reached maximum attempts try to relogin :")
                    continue
            elif relog==2:

                randint=random.randint(1000, 1999)
                print(randint)
                if int(input("Please type the above Number to continue: "))==randint:
                    print("Your Password is: "+forgotpwd(uname))
                else:
                    print(":( Entered Integer is Wrong :(")
                    continue
            elif relog==3:
                if str(input("Register the same username and password (y/n): "))=="y":
                    register(uname,passwd)
                else:
                    uname=input("Enter Username: ")
                    passwd=input("Enter Password: ")
                    register(uname,passwd)
            elif relog==4:
                print("Thanks For Using the App ")
                break
            else:
                print("Wrong option selected goint to main menu :(")

    elif choice == 3:
        print("Thanks For Using the App")
        break
    else:
        print("Please enter a correct option and continue")