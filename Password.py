#Password pass for my Truth or Dare game
print ("This level's been locked by the administrator. To proceed, you need a four digits code. If you do not have that code, please contact the administrator for it, thanks") 
input () 
Password = 2564
Number_Of_Tries = 0
Password1 = int (input ("Please enter password to proceed: "))
if Password1 == Password and Number_Of_Tries < 2:
    Number_Of_Tries = Number_Of_Tries + 1
    print ("You've entered the right password")
    input () 
    print ("You can now access the extreme level.") 
else:
    loop = True
    while loop:
        if Password1 != Password and Number_Of_Tries < 2:
            print ("You've entered the wrong password")
            Number_Of_Tries = Number_Of_Tries + 1
            Password1 = int (input ("Re-enter password: "))
            if Password1 == Password:
                print ("You've entered the right password")
                input ()
                print ("You can now access the extreme level.") 
                
                print ("Now let's proceed with the game") 
        
        else:
            Number_Of_Tries = Number_Of_Tries + 1
            if Password1 != Password and Number_Of_Tries > 2:
                print ("Too many failed attempts, please contact administrator")
                break
           
