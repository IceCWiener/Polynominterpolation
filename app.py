import os
import easygui

msg = "lädt..."
title = "Interpolation - Numerische Algorithmen"
choices = ["Test1", "Test2", "PuTTY"]
reply = easygui.buttonbox(msg,  title, choices = choices)

if reply == "PuTTY":
    os.system("putty")
else:
    print("done")