# program to generate random password
from tkinter import *
import random
import string


def ranpwd():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
        string.digits) + random.choice(['@', '#', '$', '%', '&', '!'])
    for i in range(6):
        password += random.choice(randomSource)
    listBox.set('')
    listBox.set(password)


root = Tk()
root.title('Password Generator')
root.geometry('300x100')

pwddis = Frame(root)
pwddis.pack()

butn = Frame(root)
butn.pack()

# Password Display
listBox = StringVar()
listB = Entry(pwddis, textvariable=listBox, width=20, bd=2)
listB.grid(row=0, column=0, pady=20, padx=10)
listButton = Button(butn, text='Generate', command=ranpwd)
listButton.grid(row=0, column=0)

# Reset & Exit Buttons
quitButton = Button(butn, text='Exit', padx=20, command=root.quit)
quitButton.grid(row=0, column=1)

root.mainloop()
