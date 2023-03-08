#random password generator using python

import random

Numbers = "0123456789" 
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "?/\:*#$&%"

combination = Numbers + lower_case + upper_case + symbols
length_of_password = 10

for i in range (0, 20):
    Password = "".join(random.sample(combination, length_of_password))
    print ("Your Generated Password Is: " + Password)
    