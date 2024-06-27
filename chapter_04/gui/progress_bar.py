from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 50
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value'] += speed / GB * 100
        download += speed
        percent.set('{}%'.format(int(download/GB * 100)))
        text.set('{}/{} gigabytes downloaded'.format(download, GB))
        window.update_idletasks()
        window.update()


window = Tk()
window.geometry('350x300')

percent = StringVar()
percent.set('I has not been initiated')

text = StringVar()

bar = Progressbar(window, orient='horizontal', length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text='download', command=start)
button.pack()

window.mainloop()
