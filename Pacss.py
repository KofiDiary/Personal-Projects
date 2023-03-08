print ("Enter Number Of User")
Number = input ()
while len (Number) > 10 or len (Number) < 10:
    print ("Number should be 10 digits. Re-enter number")
    Number = input () 
    if len (Number) == 10:
        break

print ("Confirm Number")
Number1 = input ()
while len (Number1) > 10 or len (Number1) < 10:
    print ("Number should be 10 digits. Re-enter number")
    Number1 = input () 
    if len (Number1) == 10:
        break
       
Loop = True
while Loop:
    if Number!= Number1:
        print ("Number mis-match. Re-enter number of user")
        Number = input () 
        print ("Confirm number") 
        Number1 = input () 
        if Number == Number1:
            break
    else:
        if Number == Number1:
            break

print ("You have requested to send money to so so and so person")