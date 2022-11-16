import os
import easygui
#from hermite import Hermite
from tabulate import tabulate


def newton():
    msg = "lädt..."
    title = "Interpolation - Numerische Algorithmen"
    choices = ["Test1", "Test2", "PuTTY"]
    reply = easygui.buttonbox(msg,  title, choices=choices)

    if reply == "PuTTY":
        os.system("putty")
    else:
        print("done")


def hermite():
    print("selected hermite")


def input_table():
    input_table = []
    i = 0
    while i < 3:
        print("Bitte einen x-Wert angeben: ")
        input_table.append(tuple([input(), ]))
        print(input_table)
        print("Bitte einen y-Wert oder eine Steigung angeben: ")
        input_table[i] = input_table[i] + (input(),)
        print(input_table)
        i = i+1

    print("Bitte 1 angeben, wenn hermite, also 2 gleiche Stützstellen hintereinander kommen: ")
    userInput = input()
    if (userInput == "1"):
        print("here comes hermite :)")
        #local_hermite = Hermite(inputTable)
        #print(local_hermite)


if __name__ == '__main__':
    input_table()

