#!/usr/bin/python3
from tkinter import *
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


def generate():
    kind = keys.get()
    word = ""
    if kind == "1":
        word = letters(int(length.get()))
    elif kind == "2":
        word = letters_2(int(length.get()))
    result.insert(END, "\n " + word)


root = Tk()
root.title("Random word")
root.configure(background="black")
text_color = "#fff"
background_color = "#000"
Label(root, text="Random word", font=("Lucida Sans", 30), bg=background_color, fg=text_color).pack()
aaa = Frame(root, bg=background_color)
aaa.pack()
bbb = Frame(aaa, bg=background_color)
bbb.grid(row=0, column=0)
ccc = Frame(aaa, bg=background_color)
ccc.grid(row=1, column=0)
Label(bbb, text="Word from latin letters -> '1'.", bg=background_color, fg=text_color).pack()
Label(bbb, text="Word, same num. of consonants and vowels -> '2'.", bg=background_color, fg=text_color).pack()
Label(ccc, text="Type: ", bg=background_color, fg=text_color).grid(row=0, column=0)
keys = Entry(ccc, bg=background_color, fg=text_color)
keys.grid(row=0, column=1)
Label(ccc, text="Length: ", bg=background_color, fg=text_color).grid(row=1, column=0)
length = Entry(ccc, bg=background_color, fg=text_color)
length.grid(row=1, column=1)
Button(root, text="Generate", bg=background_color, fg=text_color, command=lambda: generate()).pack()
result = Text(root, bg=background_color, fg=text_color)
result.pack()
Button(root, text="Turn off", command=lambda: root.destroy(), bg=background_color, fg=text_color).pack()
root.mainloop()

