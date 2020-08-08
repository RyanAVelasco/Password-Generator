import random
import string
from tkinter import *

temp = list()

root = Tk()
root.title("Password Generator")
root.geometry("150x250")

a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()

letter_lower = Label(root, text="Lowercase Letters (a-z)").pack()
letter_lower_entry = Checkbutton(root, text="", variable=a).pack()

letter_uppercase = Label(root, text="Uppercase Letters (A-Z)").pack()
letter_uppercase_entry = Checkbutton(root, text="", variable=b).pack()

digits = Label(root, text="Digits (0-9)").pack()
digits_entry = Checkbutton(root, text="", variable=c).pack()

punctuation = Label(root, text="Symbols (@,%,..)").pack()
punctuation_entry = Checkbutton(root, text="", variable=d).pack()

# length = Label(root, text="Please enter desired length: ").pack(pady=5)
# length_entry = Entry(root, text="").pack()

generate = Button(root,
                  text="GENERATE PASSWORD",
                  command=lambda: check_button(letter_lower_entry,
                                               letter_uppercase_entry,
                                               digits_entry,
                                               punctuation)).pack(pady=5)

password = Entry(root, text="")
password.pack()




def check_button(lower, upper, digit, symbol):
    global temp
    gen = 0

    password.delete(0, "end")

    while gen < 16:
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