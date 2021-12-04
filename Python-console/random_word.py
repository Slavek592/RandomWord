#!/bin/python
from Definitions import random_letters
from Definitions import special

print("Hello!")
print("Chose kind of word making.")
kind = ""
while True:
    kind = str(input("If You want a word made from random latin letters, print '1'. If you want a word, where is"
                     " approximately same number of consonants and vowels, print '2'. If you want a word, where every"
                     " second letter is vowel and every second is consonant, print '3'. If you want a word, that seems"
                     " to be a word from some language, print '4'."))
    if kind in ["1", "2", "3", "4"]:
        break
    else:
        print("Unknown command.")
while True:
    try:
        length = int(input("How many letters?"))
        if length > 100:
            print("Too many.")
        else:
            break
    except ValueError:
        print("Input must be a string.")
keys = ""
while kind == "4":
    print("Type your language. English, Czech, German and Russian are supported.")
    language = str(input("")) + "\n"
    keys = special.load_keys(language, "Data/Languages.txt")
    if language in ["English\n", "Czech\n", "German\n", "Russian\n"]:
        break
    else:
        print("This language is not supported. Try writing one of the supported four."
              " Start the name with capital.")
while True:
    word = ""
    if kind == "1":
        word = random_letters.letters(length)
    elif kind == "2":
        word = random_letters.letters_2(length)
    elif kind == "3":
        word = random_letters.word(length)
    elif kind == "4":
        word = special.special_word(length, keys)
    print(word)
    end = str(input("Print \"end\" to end."))
    if end in ["1", "e", "end", "exit", "q", "quit"]:
        break
print("Thank You for using.")
print("Made by Viacheslav Nikiforov.")
