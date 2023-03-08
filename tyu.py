print ("Hello what's your name?")
player_name = input ()
import random
number = random.randint(1, 5)
number_of_guesses = 0
print ("Okay", player_name, "guess a number between 1 to 5")
while number_of_guesses < 5:
    guess = int (input ())
    number_of_guesses = number_of_guesses + 1
    if guess < number:
        print ("Your guess is too low")
    if guess > number:
        print ("Your guess is too high")
    if guess == number:
        break
if guess == number:
    print ("You guessed the number right in", str(number_of_guesses), "tries")
else:
    print ("You failed to guess the right number. The right number is", str(number))
