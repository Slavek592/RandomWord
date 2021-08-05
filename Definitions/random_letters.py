#!/bin/python
from random import randint


def letters(a, capital=True):
    final_name = ""
    big_keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                "T", "U", "V", "W", "X", "Y", "Z"]
    small_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                  "t", "u", "v", "w", "x", "y", "z"]
    for i in range(a):
        if capital and i == 0:
            final_name += big_keys[randint(0, 25)]
        else:
            final_name += small_keys[randint(0, 25)]
    return final_name


def word(a, capital=True):
    final_name = ""
    big_keys = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    small_keys = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    vowel_keys = ["a", "e", "i", "o", "u", "y"]
    for i in range(a):
        if i % 2 == 0:
            if capital and i == 0:
                final_name += big_keys[randint(0, 19)]
            else:
                final_name += small_keys[randint(0, 19)]
        else:
            final_name += vowel_keys[randint(0, 5)]
    return final_name


def letters_2(a, capital=True):
    final_name = ""
    big_keys = ["A", "A", "A", "B", "C", "D", "E", "E", "E", "F", "G", "H", "I", "I", "J", "K", "L", "M", "N",
                "O", "O", "P", "R", "S", "T", "U", "U", "V", "Y", "Y", "Z"]
    small_keys = ["a", "a", "a", "b", "c", "d", "e", "e", "e", "f", "g", "h", "i", "i", "j", "k", "l", "m", "n",
                  "o", "o", "p", "r", "s", "t", "u", "u", "v", "y", "y", "z"]
    for i in range(a):
        if capital and i == 0:
            final_name += big_keys[randint(0, 30)]
        else:
            final_name += small_keys[randint(0, 30)]
    return final_name
