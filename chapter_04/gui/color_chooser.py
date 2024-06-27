from tkinter import *
from tkinter import colorchooser  # submodule


def choose():
    # color = colorchooser.askcolor()
    # colorHex = color[1]
    # window.config(background=colorHex)

    window.config(background=colorchooser.askcolor()[1])


window = Tk()
window.geometry('420x420')

button = Button(window, text='click me', command=choose)
button.pack()


window.mainloop()
