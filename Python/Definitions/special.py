#!/bin/python
from random import randint


def load_keys(massif, file_name):
    open_file = open(file_name)
    found = 0
    keys = [[], []]
    current_number = 0
    for read_line in open_file:
        if found == 1 and read_line != "\n":
            letter = ""
            number = ""
            found_2 = 0
            for read_letter in read_line:
                if found_2 == 1 and read_letter != "\n":
                    number += read_letter
                elif read_letter == " ":
                    found_2 = 1
                elif read_letter != "\n":
                    letter += read_letter
            current_number += int(number)
            keys[0].append(current_number)
            keys[1].append(letter)
        elif read_line == massif:
            found = 1
        elif found == 1 and read_line == "\n":
            break
    return keys


def special_word(length, keys):
    word = ""
    number_of_letters = 0
    for read_number in keys[0]:
        number_of_letters += 1
    for i in range(length):
        random = randint(0, keys[0][number_of_letters-1])
        for j in range(number_of_letters):
            if keys[0][j] >= random:
                word += keys[1][j]
                break
    return word


def special_word_main(length):
    language = input("Type your language.") + "\n"
    keys = load_keys(language, "Data/Languages.txt")
    word = special_word(length, keys)
    return word
