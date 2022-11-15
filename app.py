import os
import easygui
from hermite import Hermite


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


def menu():
    print("Bitte 1. x-Wert angeben: ")
    input1 = input()
    print("Bitte 1. y-Wert angeben: ")
    input2 = input()

    print("Bitte nochmal den 1. x-Wert angeben: ")
    input3 = input()

    print("Bitte die Ableitung an Stelle x0 angeben: ")
    input4 = input()

    print("Bitte 2. x-Wert angeben: ")
    input5 = input()
    print("Bitte 2. y-Wert angeben: ")
    input6 = input()

    print("Bitte 1 angeben, wenn hermite, also 2 gleiche Stützstellen hintereinander kommen: ")
    userInput = input()
    if (userInput == "1"):
        local_hermite = Hermite(input1, input2, input3, input4, input5, input6)
        print(local_hermite)

if __name__ == '__main__':
    menu()

