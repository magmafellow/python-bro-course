from tkinter import *


inWindow = False


def doSomething(event):
    global inWindow
    print('Mouse coordinates [{},{}]'.format(event.x, event.y))
    # inWindow = not inWindow
    # print('Is it in window now? = {}'.format(inWindow))


window = Tk()

# Button-1 = left click
# Button-2 = middle-scroll click
# Button-3 right click
# window.bind('<Button-1>', doSomething)
# window.bind('<ButtonRelease>', doSomething)
# window.bind('<Enter>', doSomething)  # Do not confuse 'Enter' with Enter key. 'Enter' is where you come in window
# window.bind('<Leave>', doSomething)
window.bind('<Motion>', doSomething)  # Where the mouse moved


window.mainloop()
