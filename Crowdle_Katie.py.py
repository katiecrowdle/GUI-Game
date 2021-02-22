from tkinter import *
import random
from time import *

# outside
root = Tk()
root.title("Katie's Game")
root.geometry("680x680")

# background
root.minsize(height=200, width=300)
root.configure(bg="#304C89", pady=50)

frame = Frame(root)
frame.config(bg="pink", pady=20)

# Pick a colour label
label2 = Label(frame, width=17, height=3, text="Please pick a colour:", bg="pink")
label2.grid(row=0, column=1)


# Colour box
e = Entry(frame, width=17, bg="pink", bd=3, justify=CENTER)
e.grid(row=0, column=2)


# Start Game
def play():
    global t1
    colour = e.get()
    if colour == "":
        colour = "pink"
    xpos = random.randint(1, 470)
    ypos = random.randint(1, 420)
    char = canvas.create_rectangle(xpos, ypos, xpos + 30, ypos + 30, fill=str(colour))
    t1 = round(time() * 1000)
    canvas.tag_bind(char, '<ButtonPress-1>', ObjectClick)


def ObjectClick(event):
    canvas.delete('all')
    t2 = round(time() * 1000)
    if int(Counter.__str__(counter)) <= 10:
        if t2-t1 <= 2000:
            addcounter(counter)
    elif 10 < int(Counter.__str__(counter)) <= 20:
        if t2-t1 <= 2000:
            addcounter(counter)
    elif 20 < int(Counter.__str__(counter)) <= 30:
        if t2-t1 <= 2000:
            addcounter(counter)
    elif 30 < int(Counter.__str__(counter)) <= 40:
        if t2-t1 <= 2000:
            addcounter(counter)
    elif 40 < int(Counter.__str__(counter)) < 50:
        if t2-t1 <= 2000:
            addcounter(counter)
    elif int(Counter.__str__(counter)) >= 50:
        addcounter(counter)
        label2 = Label(frame, height=3, width=40, bg="lightgreen", text="Congratulations you got to 50! YOU WIN")
        label2.grid(row=5, column=2)

    canvas.tag_bind('<ButtonPress-1>', play())


# Start Game button
button = Button(frame, bg="#AFCBFF", activeforeground="blue", height=2, width=15, padx=5, pady=5,text="Start Game!", command=play)
button.grid(row=0, column=3)

# Counter
class Counter(object):
    def __init__(self):
        self._counter = 0

    @property
    def counter(self):
        return self._counter

    def increment(self):
        self._counter += 1

    def __str__(self):
        string = "{}".format(self._counter)
        return string


def addcounter(event):
    counter.increment()
    label()


# Counter Label
counter = Counter()
label1 = Label(frame, height=3, width=17, bg="pink", text="Total Score: " + str(0))
label1.grid(row=0, column=4)


def label():
    number = Counter.__str__(counter)
    label1.configure(text="Total Score: " + number)
    label1.grid(row=0, column=4)


# foreground
canvas = Canvas(root, cursor="heart", bg="#AFCBFF", width=500, height=450)
canvas.pack(side=BOTTOM)

frame.pack(side=TOP)
root.mainloop()




