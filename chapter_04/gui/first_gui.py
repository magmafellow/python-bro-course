from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()       # instantiate an instance of a window

window.geometry('420x420')
window.title('Bro works great for me!')

icon = PhotoImage(file='variant2-rose.png')
window.iconphoto(True, icon)

window.config(background='#333000')


window.mainloop()   # place window on computer screen, listen for events
