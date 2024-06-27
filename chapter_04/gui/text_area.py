# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *


def submit():
    input = text.get('1.0', END)
    print(input)


window = Tk()
# window.geometry('420x420')
window.title('Textarea practice')

text = Text(
    window,
    bg='light yellow',
    font=('Ink Free', 25, 'bold'),
    height=8,
    width=20,
    fg='crimson',
    padx=20,
    pady=20,
)
text.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
