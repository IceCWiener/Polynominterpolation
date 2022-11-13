import os
import easygui


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
    print("Please enter 1, 2 3 to choose an option: ")

    print("1) Newton \n2) Hermite \n3) Exit")
    userInput = input()

    if userInput == "1":
        newton()

    if userInput == "2":
        hermite()

    if userInput == "3":
        print("Goodbye :)")
        exit()


if __name__ == '__main__':
    menu()

