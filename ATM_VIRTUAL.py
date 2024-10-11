import random
print("Welcome To SBI ATM:")
while True:
    login=int(input("enter only 16 digit Login ID:"))
    password=input("Enter the Bank Password String:")
    if len(str(login))==16:
        print("login is successfully Verified")
        break
    else:
        print("Login is Failed")
        print("Please enter the correct login id ")
    
a=random.randint(0000,9999)
print("The Bank OTP is SENT Successfully To You:",a)

Balance=5000
 
def Bank_Balance():
    print("Your Bank Balance:",Balance)

def Amount_Withdrawal():
    global Balance
    while True:
        pin = input("Enter the 4-digit Account PIN: ")
        if len(pin) == 4:
            print("The Account PIN is Verified")
            amount = int(input("Enter the Amount to Withdraw: "))
            if amount <= Balance:
                Balance -= amount  
                print(f"Transaction successful! Your Bank Balance: {Balance}")
            else:
                print("Insufficient balance")
            break
        else:
            print("The Account PIN is incorrect")
            print("Please enter the correct Account Pin")

def Amount_Added():
    global Balance
    while True:
        pin = input("Enter the 4-digit Account PIN: ")
        if len(pin) == 4:
            print("The Account PIN is Verified")
            amount_add = int(input("Enter the Amount to Add: "))
            Balance += amount_add 
            print(f"Transaction successful! Your Bank Balance: {Balance}")
            break
        else:
            print("The Account PIN is incorrect")
            print("Please enter the correct Account Pin")


def update():
    while True:
        login_updated=int(input("Enter the login id to be updated:"))
        if len(str(login_updated))!=16:
            print("Again select the update option")
            print("Enter the Login ID correctly")
            break
        password_updated=input("Enter the password to be Updated:")
        pin_updated=int(input("Enter the pin to be updated:"))
        if len(str(pin_updated))!=4:
            print("Again select the update option")
            print("Enter the correct pin")
        update_dict={'login':login_updated,'password':password_updated,'pin':pin_updated}
        print(update_dict)
        break

def complaint():
    complaint=input("Enter the qureyes or complaintes about the bank:")
    complaint_sent="The complaint reported successfully"
    print(complaint)
    print(complaint_sent)
    contact_ph=12345678910
    contact_email='sbibank@gmail.com'
    print(contact_ph)
    print(contact_email)

s='y'
while s:
    print("Bank Details")
    print("1.Bank_Balence\n2.Amount_Widrawal\n3.Amount_ADDED\n4.update\n5.complaint")
    ch=int(input("Enter the option:"))
    if ch==1:
        Bank_Balance()
    elif ch==2:
        Amount_Withdrawal()
    elif ch==3:
        Amount_Added()
    elif ch==4:
        update()
    elif ch==5:
        complaint()
    else:
        print("Invalid option")
        s = input("DUWTC to Modules? y/n:")
        if s=='y':
            continue
        else:
            print("Thank You")
            break 




    
 



        


