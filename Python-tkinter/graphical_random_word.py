#!/usr/bin/python3
from Definitions import random_letters
from tkinter import *


def generate():
    kind = keys.get()
    word = ""
    if kind == "1":
        word = random_letters.letters(int(length.get()))
    elif kind == "2":
        word = random_letters.letters_2(int(length.get()))
    elif kind == "3":
        word = random_letters.word(int(length.get()))
    result.insert(END, "\n" + word)


root = Tk()
root.title("Random word")
root.configure(background="black")
text_color = "#fff"
background_color = "#000"
Label(root, text="Random word", font=("Lucida Sans", 60), bg=background_color, fg=text_color).pack()
aaa = Frame(root, bg=background_color)
aaa.pack()
bbb = Frame(aaa, bg=background_color)
bbb.grid(row=0, column=0)
ccc = Frame(aaa, bg=background_color)
ccc.grid(row=0, column=1)
Label(bbb, text="If You want a word made from random latin letters, print '1'.", bg=background_color, fg=text_color).pack()
Label(bbb, text="If you want a word, where is approximately same number of consonants and vowels, print '2'.", bg=background_color, fg=text_color).pack()
Label(bbb, text="If you want a word, where every second letter is vowel and every second is consonant, print '3'.", bg=background_color, fg=text_color).pack()
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

