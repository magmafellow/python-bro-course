from tkinter import *



def display():
    if x.get():
        print('You agree')
    else:
        print('You dont agree')


window = Tk()

photo = PhotoImage(file='py_logo.png')

x = BooleanVar()


check_button = Checkbutton(
    window,
    text='I agree with something',
    variable=x,
    onvalue=True,
    offvalue=False,
    command=display,
    font=('Arial', 20,),
    compound=LEFT,
    fg='#00aa00',
    bg='#003300',
    activeforeground='#00aa00',
    activebackground='#002200',
    padx=25,
    pady=10,
    image=photo,
)

check_button.pack()


window.mainloop()
