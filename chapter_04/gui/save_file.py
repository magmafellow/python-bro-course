from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    initialdir='C:\\Users\\magma\\Desktop\\Middle\\Courses\\python-bro-course\\chapter_04\\gui',
                                    filetypes=[
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('All files', '.*')
                                    ])
    if file is None:
        return

    filetext = str(text.get(1.0, END))
    # filetext = input('Enter some text I guess: ')  # use this if you want to use console
    file.write(filetext)
    file.close()


window = Tk()

button = Button(window, text='save', command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
