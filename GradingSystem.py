Scores = 0
Number = 1
print ("Enter your exam scores")
Scores = int (input ())
while Scores < 101 and Number < 51:
    if Scores < 25:
        print ("F")
    elif Scores >= 25 and Scores < 45:
        print ("E")
    elif Scores >= 45 and Scores < 50:
        print ("D")
    elif Scores >= 50 and Scores < 60:
        print ("C")
    elif Scores >= 60 and Scores <= 80:
        print ("B")
    else:
        print ("A")
    Number = Number + 1
    print ("Enter your exam scores")
    Scores = int (input ())
    if Number > 50:
        break


    
