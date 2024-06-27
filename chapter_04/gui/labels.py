from tkinter import *


# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='variant1.png', width=550, height=330)


window.geometry('800x500')
window.config(bg='#003300')

label = Label(
    window,
    text='Halo!',
    font=('Arial', 40, 'bold'),
    fg='#009900',
    bg='#006600',
    relief=RAISED,
    bd=10,
    padx='20px',
    pady='8px',
    image=photo,
    compound='bottom'
)
label.pack()
# label.place(x=100, y=100)


window.mainloop()
