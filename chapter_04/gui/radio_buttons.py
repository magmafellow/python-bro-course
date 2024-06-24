# radio buttons = similar to checkbox, but you can only select one from a group


from tkinter import *


def order():
    if x.get() == 0:
        print('You chose pizza')
    elif x.get() == 1:
        print('You chose hamburger')
    elif x.get() == 2:
        print('You ordered a hotdog')


food = [
    'pizza',
    'hamburger',
    'hotdog',
]

window = Tk()

pizza_img = PhotoImage(file='pizza.png')
hamburger_img = PhotoImage(file='hamburger.png')
hotdog_img = PhotoImage(file='hotdog.png')
food_images = [
    pizza_img, hamburger_img, hotdog_img,
]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index],  # adds text to radio buttons
        variable=x,        # groups radiobuttons together if they share the same variable
        value=index,       # assigns each radio button a different value
        padx=25,           # adds padding on x-axis
        pady=10,
        font=('Impact', 50),
        image=food_images[index],  # adds image to radio button
        compound='left',
        indicatoron=True,  # property for showing indicator
        command=order      # set command of radiobutton to function
    )
    radiobutton.pack(anchor=W)


window.mainloop()
