print ("Hello there, my name is Diary. What about you?")
Name = input ()
print ("Hello,", Name, "how are you doing?")
Response = input ()
if Response == "Fine" or Response == "Good" or Response == "Great" or Response == "I am fine" or Response == "I am good" or Response == "I am great" or Response == "I'm good" or Response == "I'm fine" or Response == "I'm great" or Response == "fine" or Response == "good" or Response == "great":
    print ("We thank God")
    input ()
    print (Name, "wanna try something fun?")
else:
    print ("Aww, what's wrong with you dear?")
    answer = input ()
    print ("Sorry for that. I pray you feel good soon!")
    input ()
    print ("Hey, I know you are not feeling good but would you like to try something fun? It might help brighten up your mood")
    answer1 = input ()
    if answer1 == "yes" or answer1 == "Yes" or answer1 == "Yeah" or answer1 == "yeah" or answer1 == "Sure" or answer1 == "sure":
        print ("Okay,", Name, "what game would you like to play? Choose from the list below...")
        Answer = ["Riddles", "Pick The Odd One Out", "Questions and Answers", "Maths", "Wordle"]
        for Ans in Answer:
            print (Ans)
