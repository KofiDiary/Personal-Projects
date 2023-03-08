print ("Hello Johnny Torgbegah. My name is Diary. How are you doing today?")
health = input ()
if health == "I am fine" or health == "I'm fine" or health == "I'm good" or health == "I'm great" or health == "I am good" or health == "I am great" or health == "Fine" or health == "fine" or health == "Good" or health == "good":
    print ("Okay, we thank God.")
else:
    print ("Aww, what's wrong?")
    input ()
    print ("Hmm, I pray you feel better soon (:")
    
print ("So, Johnny, how may I be of help to you today?")
input ()
print ("Umm... didn't catch that. Sorry. Re-send message")
input ()
print ("Here's a list of the things I can do...")
do = ["Calculate Density", "Calculate Velocity", "Find the largest of three numbers"]
for d in do:
    print (d)
input ()
print ("Sorry, didn't catch that. Send reply in this format; Density, Velocity or Largest of Three Numbers")
ans = input ()
if ans == "Density":
    print ("Okay, enter the value of Density, Volume or Mass. Enter 0 if you don't have the value for a specific quantity")
    Volume = input ("Input value of Volume: ")
    Mass = input ("Input value of Mass: ")
    if int (Density) != 0 and int (Volume) == 0:
        print (int (Mass) / int (Density))
    elif int (Density) == 0 and int (Mass) != 0 and int (Volume) != 0:
        print (int (Mass) / int (Volume))
    else:
        print (int (Density) * int (Volume))
elif ans == "Velocity":
    print ("Okay send me the value of time, displacement or velocity. Enter 0 if you don't have the value of a particular quantity")
    Density = input ("Input the value of Density: ")
    Velocity = input ("Input the value of Velocity: ")
    Time = input ("Input the value of Time: ")
    Displacement = input ("Input the value of Displacement: ")
    if int (Velocity) != 0 and int (Time) == 0:
        print (int (Displacement) / int (Velocity))
    elif int (Velocity) == 0 and int (Displacement) != 0 and int (Time) != 0:
        print (int (Displacement) / int (Time))
    else:
        print (int (Velocity) * int (Time))
elif ans == "Largest of Three Numbers":
    print ("Oh okay, enter any 3 numbers to compare")
    A = input ()
    B = input ()
    C = input ()
    if int (A) > int (B) and int (A) > input (C):
        print (A)
    elif int (A) < int (B) and int (B) > int (C):
        print (B)
    else:
        print (C)
else:
    print ("Umm... please re-enter reply")
