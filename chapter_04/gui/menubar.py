from tkinter import *


def openFile():
    print('File has been opened')


def saveFile():
    print('File has been saved')


def cut():
    print('Text has been cut')


def copy():
    print('Text has been copied')


def paste():
    print('Text has been pasted')


window = Tk()

openImage = PhotoImage(file='cold.png')
exitImage = PhotoImage(file='fire.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=False, font=('consolas', 14))
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', image=openImage, compound='left', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', image=exitImage, compound='right', command=quit)

editMenu = Menu(menubar, tearoff=False, font=('consolas', 14))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)

window.mainloop()
