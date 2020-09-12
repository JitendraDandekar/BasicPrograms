from tkinter import *
import random

root = Tk()
root.geometry("300x350")
root.title("Rolling Dice")
photo = PhotoImage(file = "dice5.png")
root.iconphoto(False, photo)

header = Label(root, text="Hello..!!", font="Times 25 bold")
header.pack(pady=10)

#Images
dice = ['dice1.png','dice2.png','dice3.png','dice4.png','dice5.png','dice6.png']
diceImage = PhotoImage(file = (random.choice(dice)))

#widget for image
img = Label(root, image=diceImage)
img.image = diceImage
img.pack(expand=True)

#Function after button clicked
def rolling():
    diceImage = PhotoImage(file = (random.choice(dice)))
    img.configure(image=diceImage)
    img.image = diceImage
    
btn = Button(root, text="Click Me!", font="Times 20 bold", command=rolling)
btn.pack(pady=10)

root.mainloop()
