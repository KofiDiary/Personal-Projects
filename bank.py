print ("Welcome to Diary Bank. Please insert your card to continue...")
action = input ()
if action == "insert" or action == "Insert":
    print ("Please enter your password to continue")
    password0 = int (input())
    password1 = 2564
    number = 0
    while password0 != password1 and number < 3:
        print ("You have entered the wrong password")
        password0 = int (input ("Re-enter your password: "))
        if password0 == password1:
            break
        else:
            number = number + 1
            if number >= 3:
                print ("Dear valued customer, your account has been blocked. Please contact customer care.")
                break
