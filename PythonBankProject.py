print ("Welcome to Diary Bank Of Ghana. Please insert your card to proceed")
action = input ()
if action == "insert" or action == "Insert":
    password = 2564
    print ("Enter your password to proceed")
    password = int (input ())
    while password != 2564:
        print ("You have entered the wrong password")
        password = int (input ("Re-enter your password: "))
        if password == 2564:
            break
    print ("You have entered the correct password")
    to_do = ["Withdraw Cash", "Check Balance", "Change Pin"]
    for todo in to_do:
        print (todo)
    choice = input ()
    if choice == "Withdraw cash" or choice == "Withdraw Cash" or choice == "withdraw cash":
        print ("Enter amout amount to withdraw")
        Amount = int (input ())
        Balance = 3500
        Limit = 2500
        if Amount > Limit and Amount > Balance:
            print ("You have insufficient funds to perform this transaction")
            input ()
        elif Amount > Limit and Amount < Balance:
            print ("Your transaction has failed because your daily limit is GhS 2,500.00")
            input ()
        else:
            print ("Wait while we process your transaction...")
            print ("Please remove your card from the slot and take your cash")
            print ("Thank You for banking with us")
            input ()
    elif choice == "Check Balance" or choice == "check balance" or choice == "Check balance":
        print ("Your Balance Is GHS 3,500.00")
        print ("Thank You For Banking With Us")
        input ()
    elif choice == "Change pin" or choice == "Change Pin" or choice == "change pin":
        print ("Enter old password to continue")
        oldpassword = int (input ())
        while oldpassword != password:
            print ("The password you entered doesn't match your old password")
            oldpassword = int (input ("Re-enter your old password: "))
            if oldpassword == password:
                break
        print ("Now, enter your new password")
        newpassword1 = int (input ())
        print ("Confirm new password")
        newpassword2 = int (input ())
        while newpassword1 != newpassword2:
            print ("Your password doesn't match")
            newpassword1 = int (input ("Re-enter new password: "))
            newpassword2 = int (input ("Confirm new password: "))
            if newpassword1 == newpassword2:
                break
        print ("Your pin has been changed successfully")
        print ("Thank you for banking with us.")
        input ()
    else:
        print ("):")
        input ()
else:
    print ("Thank You For Banking With Us. We Hope To See You Again Soon :)")
    input ()
            
        
        
