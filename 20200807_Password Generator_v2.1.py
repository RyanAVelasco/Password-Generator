import random
import string
from tkinter import *

temp = list()

root = Tk()
root.title("Password Generator")

a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()

letter_lower = Label(root, text="Lowercase Letters (a-z)").grid(row=0, column=0)
letter_lower_entry = Checkbutton(root, text="", variable=a)
letter_lower_entry.grid(row=0, column=1)

letter_uppercase = Label(root, text="Uppercase Letters (A-Z)").grid(row=1, column=0)
letter_uppercase_entry = Checkbutton(root, text="", variable=b)
letter_uppercase_entry.grid(row=1, column=1)

digits = Label(root, text="Digits (0-9)").grid(row=2, column=0)
digits_entry = Checkbutton(root, text="", variable=c)
digits_entry.grid(row=2, column=1)

punctuation = Label(root, text="Symbols (@,%,..)").grid(row=3, column=0)
punctuation_entry = Checkbutton(root, text="", variable=d)
punctuation_entry.grid(row=3, column=1)

length = Label(root, text="PASSWORD LENGTH: ").grid(row=4, column=0, pady=5)
length_entry = Entry(root, text="")
length_entry.grid(row=4, column=1)

o = Button(root, text="GENERATE PASSWORD", command=lambda: check_button(length_entry))\
    .grid(row=5, column=0, columnspan=2, pady=5)

password = Entry(root, text="")
password.grid(row=6, column=0, columnspan=2, pady=10)


def check_button(length):
    global temp

    gen = 0
    size = int(length.get())

    password.delete(0, "end")

    if size < 1:
        print("Value > 1 and at least one checked box")
    else:
        while gen < size:
            n = random.randint(0, 3)
            if n == 0:
                if a.get() == 1:
                    temp.append(random.choice(string.ascii_lowercase))
                    gen += 1
            if n == 1:
                if b.get() == 1:
                    temp.append(random.choice(string.ascii_uppercase))
                    gen += 1
            if n == 2:
                if c.get() == 1:
                    temp.append(random.choice(string.digits))
                    gen += 1
            if n == 3:
                if d.get() == 1:
                    temp.append(random.choice(string.punctuation))
                    gen += 1

        random.shuffle(temp)

        delimiter = ""
        x = delimiter.join(temp)
        password.insert(0, x)

        temp = []


root.mainloop()