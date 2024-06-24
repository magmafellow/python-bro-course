from tkinter import *


def submit():
    print('The temperature is: {} degrees C'.format(scale.get()))


window = Tk()
window.geometry('1000x800')


scale = Scale(
    window,
    from_=100,
    to=0,
    length=500,
    orient='vertical',
    font=('Consolas', 24),
    tickinterval=10,
    showvalue=True,         # adds a numeric indicator for a value
    resolution=5,
    troughcolor='#990101',
    highlightcolor='blue',
    # fg='#223c79',
    fg='#223cbb',
    bg='#111',

)
scale.set(93)

fire = PhotoImage(file='fire.png')
Label(image=fire).pack()

scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()

cold = PhotoImage(file='cold.png')
Label(image=cold).pack()

window.mainloop()
