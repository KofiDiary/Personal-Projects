print ("Enter any 3 numbers")
A = input ()
B = input ()
C = input ()

if int (A) > int (B) and int (A) > int (C):
    print (A)
elif int (A) > int (B) and int (A) < int (C):
    print (C)
elif int (A) < int (B) and int (B) > int (C):
    print (B)
else:
    print (C)
