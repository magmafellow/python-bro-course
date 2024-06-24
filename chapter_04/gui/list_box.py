# list box = A listing of selectable text items within its own container

from tkinter import *


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print('You have ordered: ')
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(
    window,
    fg='#363001',
    bg='#d9cd64',
    font=('Constantia', 23),
    width=12,
    selectmode='multiple',
)

listbox.pack()

listbox.insert(1, 'pizza')
listbox.insert(2, 'pasta')
listbox.insert(3, 'garlic bread')
listbox.insert(4, 'soup')
listbox.insert(5, 'chiabatta')

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text='submit', command=submit)
submitButton.pack()

addButton = Button(window, text='add', command=add)
addButton.pack()

delButton = Button(window, text='del', command=delete)
delButton.pack()

window.mainloop()
