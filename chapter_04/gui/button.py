from tkinter import *


# button = you click it, then it does stuff

count = 0
def click():
    global count
    count += 1
    print(count)


window = Tk()

photo = PhotoImage(file='like_03.png', width=130, height=130)

button = Button(
    window,
    text='click me!',
    command=click,
    font=('Comic Sans', 30),
    activebackground='lightblue',
    foreground='green',
    activeforeground='blue',
    state=NORMAL,
    image=photo,
    compound=BOTTOM
)
button.pack()

window.mainloop()
