#!/bin/python
from Definitions import random_letters
from random import randint

while True:
    try:
        count = int(input("How many words?"))
        if count > 1000:
            print("Too many.")
        else:
            break
    except ValueError:
        print("Input must be a string.")
string = ""
capital = True
for word in range(count):
    string += random_letters.letters_2(randint(1, 10), capital)
    if randint(0, 9) == 0:
        string += ". "
        capital = True
    elif word != count - 1:
        string += " "
        capital = False
    else:
        string += "."
print(string)
