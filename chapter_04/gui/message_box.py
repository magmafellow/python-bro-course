from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title='This is an info message box', message='You are a person')

    # while True:
    #     messagebox.showwarning(title='Warning', message='You have a virus')
    # messagebox.showerror(title='Error 508', message='Something went wrong')

    # if messagebox.askokcancel(title='ask ok cancel', message='do you want to do the thing?'):
    #     print('You did the thing')
    # else:
    #     print('You canceled the thing')

    # if messagebox.askretrycancel(title='ask ok cancel', message='do you want to retry the thing?'):
    #     print('You retried the thing')
    # else:
    #     print('You canceled the thing')

    # if messagebox.askyesno(title='ask yes or no', message='Do you like cake?'):
    #     print('I like cake too')
    # else:
    #     print('Why do you not like cake? :(')

    # answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
    # if (answer == 'yes'):
    #     print('I like pie too :)')
    # elif answer == 'no':
    #     print('Why do you not like pie :(')

    answer = messagebox.askyesnocancel(title='ask yes no cancel', message='Do you like to code?', icon='error')
    if answer == True:
        print('That is great')
    elif answer == False:
        print('Then why are you watching a video on coding')
    else:
        print('You have dodged the question')


window = Tk()
window.title("We are working!")


button = Button(window, command=click, text='click me')
button.pack()


window.mainloop()
