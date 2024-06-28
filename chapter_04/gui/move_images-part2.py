from tkinter import *


def move_up(e):
    canvas.move(myimage, 0, -10)

def move_down(e):
    canvas.move(myimage, 0, 10)


def move_left(e):
    canvas.move(myimage, -10, 0)

def move_right(e):
    canvas.move(myimage, 10, 0)


window = Tk()

window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

window.bind('<Up>', move_up)
window.bind('<Down>', move_down)
window.bind('<Left>', move_left)
window.bind('<Right>', move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoImage = PhotoImage(file='car.png')
myimage = canvas.create_image(0, 0, image=photoImage, anchor=NW)

window.mainloop()
