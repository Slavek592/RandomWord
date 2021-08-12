#!/bin/python
from random import randint


def letters(a):
    final_name = ""
    big_keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                "T", "U", "V", "W", "X", "Y", "Z"]
    small_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                  "t", "u", "v", "w", "x", "y", "z"]
    for i in range(a):
        letter_number = randint(0, 25)
        if i == 0:
            final_name += big_keys[letter_number]
        else:
            final_name += small_keys[letter_number]
    return final_name


def make_word(a):
    final_name = ""
    big_keys = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    small_keys = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    vowel_keys = ["a", "e", "i", "o", "u", "y"]
    for i in range(a):
        if i % 2 == 0:
            letter_number = randint(0, 19)
            if i == 0:
                final_name += big_keys[letter_number]
            else:
                final_name += small_keys[letter_number]
        else:
            letter_number = randint(0, 5)
            final_name += vowel_keys[letter_number]
    return final_name


def letters_2(a):
    final_name = ""
    big_keys = ["A", "A", "A", "B", "C", "D", "E", "E", "E", "F", "G", "H", "I", "I", "J", "K", "L", "M", "N",
                "O", "O", "P", "R", "S", "T", "U", "U", "V", "Y", "Y", "Z"]
    small_keys = ["a", "a", "a", "b", "c", "d", "e", "e", "e", "f", "g", "h", "i", "i", "j", "k", "l", "m", "n",
                  "o", "o", "p", "r", "s", "t", "u", "u", "v", "y", "y", "z"]
    for i in range(a):
        letter_number = randint(0, 30)
        if i == 0:
            final_name += big_keys[letter_number]
        else:
            final_name += small_keys[letter_number]
    return final_name


print("Chose kind of word making.")
while True:
    kind = str(input("If You want a word made from random latin letters, print '1'. If you want a word, where is"
                     " approximately same number of consonants and vowels, print '2'. If you want a word, where every"
                     " second letter is vowel and every second is consonant, print '3'."))
    if kind in ["1", "2", "3"]:
        break
    elif kind == "4":
        print("Try the normal version. This short one does not have it.")
    else:
        print("Unknown command.")
while True:
    try:
        length = int(input("How many letters?"))
        if length < 100:
            break
        else:
            print("Too many.")
    except ValueError:
        print("Input must be an integer.")
while True:
    if kind == "1":
        word = letters(length)
    elif kind == "2":
        word = letters_2(length)
    elif kind == "3":
        word = make_word(length)
    print("    " + word)
    end = str(input("    "))
    if end in ["1", "e", "end", "exit", "q", "quit"]:
        break
print("Thank You for using.")
print("Made by Viacheslav Nikiforov.")
