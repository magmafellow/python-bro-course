# frame = a rectangular container to group and hold widgets

from tkinter import *


window = Tk()
window.geometry('500x500')

frame = Frame(window, bg='#666', bd=5, relief=SUNKEN, padx=10, pady=5)
# frame.pack(side=BOTTOM)
frame.place(x=100, y=100)

Button(frame, text='W', font=('Consolas', 25), width=3, fg='white', bg='#222').pack(side=TOP)
Button(frame, text='A', font=('Consolas', 25), width=3, fg='white', bg='#222').pack(side=LEFT)
Button(frame, text='S', font=('Consolas', 25), width=3, fg='white', bg='#222').pack(side=LEFT)
Button(frame, text='D', font=('Consolas', 25), width=3, fg='white', bg='#222').pack(side=LEFT)


window.mainloop()
