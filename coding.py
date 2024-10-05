import mysql.connector as m
con=m.connect(host="localhost",user="root",password="")
if con.is_connected():
    print("Host Is Connected!")
    cur=con.cursor()
    cur.execute("create database if not exists tours_travels")
    cur.execute("use tours_travels")
    cur.execute("create table if not exists Buyer(Buyer_Name varchar(20),Buyer_Phno int,Buyer_Address varchar(20),AADHAAR int(20));")
    cur.execute("create table if not exists Product(Location varchar(20),Staying_Period int(10) unique,Tour_Package varchar(20),checkout varchar(4))")
    cur.execute("create table if not exists Online_Transaction(Bank_ID int unique,UPI_ID int)")
    con.commit()

#Customer_details
def Customer_details_add():
    print("---It's time to add some details---")
    Customer_Name=input("Enter Buyer  Name:")
    Customer_Phno=int(input("Enter MobileNumber of the Buyer:"))
    Customer_Address=input("Enter Customers Address:")
    Customer_AADHAAR=input("Enter the Customer AADHAARno:")
    cur.execute("insert into Customer_details values('{}',{},'{}','{}')".format(Customer_Name,Customer_Phno,Customer_Address,Customer_AADHAAR))
    con.commit()
    print("Record Added to DataBase!")

def Customer_details_delete():
    print("---OOPS! It's deletion part---")
    Customer_Name=input("Enter Customer Name to be deleted:")
    cur.execute("delete from Customer_details where Customer_Name='{}'".format(Customer_Name))
    con.commit()
    print("Record Deleted Successfully!")

def Customer_details_update():
    print("---Hurray !! You have reached the update position---")
    print("1.CustomerName\n2.CustomerPhno\n3.CustomerAddress\n4.CustomerAADHARRno")
    ch=int(input("Enter the Choice to be selected:"))
    if ch==1:
        newv=input("Enter the Name to be updated:")
        oldv=input("Enter the old Name:")
        cur.execute("update Customer_details set Customer_Name='{}' where Customer_Name='{}'".format(newv,oldv))
        con.commit()
    elif ch==2:
        newv = int(input("Enter the PhoneNumber to be updated:"))
        oldv = int(input("Enter the old PhoneNumber:"))
        cur.execute("update Customer_details set Customer_Phno={} where Customer_Phno={}".format(newv,oldv))
        con.commit()
    elif ch==3:
        newv = input("Enter the Name to be updated:")
        oldv = input("Enter the old Name:")
        cur.execute("update Customer_details set Customer_Address='{}' where Customer_Address='{}'".format(newv,oldv))
        con.commit()
    elif ch==4:
        newv = input("Enter the Name to be updated:")
        oldv = input("Enter the old Name:")
        cur.execute("update Customer_details set Customer_AADHAARno='{}' where AADHAARno='{}'".format(newv,oldv))
        con.commit()
    else:
        print("There is no use of this option :-) ")
        s=input("DUWTC y/n:")

def Customer_details_display():
    cur.execute("select * from Customer_details")
    l=cur.fetchall()
    for i in l:
        print(i)

#Package Module
def Package_add():
    print("---It's time to add some details---")
    Location_Name=input("Enter Location Name:")
    Staying_Period=input("Enter Staying_periods:")
    Tour_Package=(input("Enter the package name:"))
    Checkout=input("Enter Yes/No :")
    cur.execute("insert into Package values('{}',{},'{}','{}')".format(Location_Name,Staying_Period,Tour_Package,Checkout))
    con.commit()
    print("Record Added to DataBase!")

def Package_delete():
    print("---OOPS! It's deletion part---")
    Staying_Period=input("Enter Staying_Period to be deleted:")
    cur.execute("delete from Package where Staying_Period='{}'".format(Staying_Period))
    con.commit()
    print("Record Deleted Successfully!")

def Package_update():
    print("---Hurray !! You have reached the update position---")
    print("1.Location_Name\n2.Staying_Period\n3.Tour_Package\n4.Checkout")
    ch = int(input("Enter the Choice to be Updated:"))
    if ch == 1:
        oldv = input("Enter the old Location Name:")
        newv = input("Enter the New Location Name to be updated:")
        cur.execute("update Package set Location_Name='{}' where Location_Name='{}'".format(newv,oldv))
        con.commit()
    elif ch == 2:
        oldv= input("Enter the old Staying_Period:")
        newv = input("Enter the Staying_Period to be updated:")
        cur.execute("update Package set Staying_period='{}' where Staying_period='{}'".format(newv,oldv))
        con.commit()
    elif ch == 3:
        oldv = int(input("Enter the old Tour_Package:"))
        newv = int(input("Enter the Tour_Package to be updated:"))
        cur.execute("update Package set Tour_Package={} where Tour_Package={}".format(newv,oldv))
        con.commit()
    elif ch == 4:
        oldv = input("Enter the Checkout:")
        newv = input("Enter the Checkout:")
        cur.execute("update Package set Permits='{}' where Checkout='{}'".format(newv,oldv))
        con.commit()
    else:
        print("There is no use of this option :-) ")
        s=input("DUWTC y/n:")

def Package_display():
    cur.execute("select * from Package")
    l = cur.fetchall()
    for i in l:
        print(i)

#Online_Transaction
def Online_Transaction_add():
    Bank_ID=int(input("Enter the Bank ID:"))    
    UPI_ID=int(input("Enter Name of the UPI ID:"))
    cur.execute("insert into Online_Transaction values({},{})".format(Bank_ID,UPI_ID))
    print("Record Added Successfully!")
    con.commit()

def Online_Transaction_delete():
    print("---OOPS! It's deletion part---")
    Bank_ID = int(input("Enter Bank-ID to be deleted:"))
    cur.execute("delete from Online_Transaction where Bank_ID={}".format(Bank_ID))
    con.commit()
    print("Record Deleted Successfully!")

def Online_Transaction_update():
    print("---Hurray !! You have reached the update position---")
    print("1.Bank ID\n2.UPI ID")
    ch=int(input("Enter the Choice to be choosen:"))
    if ch==1:
        oldv =int(input("Enter the old ID:"))
        newv=int(input("Enter the ID to be updated:"))
        cur.execute("update Online_Transaction set Bank_id={} where Bank_id={}".format(newv,oldv))
        con.commit()

    elif ch==2:
        oldv = int(input("Enter the ID:"))
        newv = input("Enter the UPI_ID to be updated:")
        cur.execute("update Online_Transaction set UPI_ID='{}' where Bank_ID={}".format(newv,oldv))
        con.commit()

    else:
        print("There is no use of this option :-) ")
        s=input("DUWTC y/n:")

def Online_Transaction_display():
    cur.execute("select * from Online_Transaction")
    l = cur.fetchall()
    for i in l:
        print(i)


#Menu
print("Tours_Travels Database!")
s='y'
while s:
    print("Modules!")
    print("1.Customer_details\n2.Package\n3.Online_Transaction")
    ch = int(input("Enter the Choice:"))
    if ch==1:
        s1='y'
        while s1=='y':
            print("This is Customer_details Table!")
            print("1.Add\n2.Delete\n3.Update\n4.Display")
            c=int(input("Enter the choice:"))
            if c==1:
                Customer_details_add()
            elif c==2:
                Customer_details_delete()
            elif c==3:
                Customer_details_update()
            elif c==4:
                Customer_details_display()
            else:
                print("No such option")
        s1=input("DUWTC")

    elif ch==2:
        s1 ='y'
        while s1 == 'y':
            print("This is Package Table!")
            print("1.Add\n2.Delete\n3.Update\n4.Display")
            c=int(input("Enter the choice:"))
            if c==1:
                Package_add()
            elif c==2:
                Package_delete()
            elif c==3:
                Package_update()
            elif c==4:
                Package_display()
            s1=input("DUWTC y/n")

    elif ch==3:
        s1 = 'y'
        while s1 == 'y':
            print("This is Online_Transaction Table!")
            print("1.Add\n2.Delete\n3.Update\n4.Display\n5.To Seek data")
            c=int(input("Enter the choice:"))
            if c == 1:
                Online_Transaction_add()
            elif c == 2:
                Online_Transaction_delete()
            elif c == 3:
                Online_Transaction_update()
            elif c == 4:
                Online_Transaction_display()
            b="y"
            while b=="y":
                
                print("1.Customer_details  Module Display\n2.Package Module")
                c = int(input("Enter the choice:"))
                if c==1:
                    print("This is Customer_details module!")
                    print("CustomerName,CustomerPhno,CustomerAddress,CustomerAADHAARno as follow:")
                    Customer_details_display()
                elif c==2:
                    print("This is Package module")
                    print("LocationName,Staying_Period,Tour_Package,Checkout as follow's:")
                    Package_display()
                else:
                    print("No such Option!")
                    b = input("DUWTC in seeking data? y/n:")
                    s1 = input("DUWTC to Customer_details module? y/n :")
                    s = input("DUWTC to Modules? y/n:")

else:
    print("Host Is Not-Connected!")
