print ("Hello there")
input ()
print ("My name is Diary. What about you?")
name = input ()
print ("Oh hey", name, "how are you doing?")
input ()
print ("I am also fine")
print ("How can I help you today?")
input ()
print ("Oh okay, I think I can help you find the density of any object")
input ()
print ("Enter the values we are going to work with; Density, Mass or Volume")
print ("Enter the Mass of the object:")
Mass = input ()
print ("Enter the Volume of the object:")
Volume = input ()
print ("Enter the Density of the object:")
Density = input ()
if int (Mass) == 0 and int (Density) != 0:
    print (int (Density) * int (Volume))
elif int (Density) != 0 and int (Volume) == 0:
    print (int (Mass) / int (Density))
else:
    print (int (Mass) / int (Volume))