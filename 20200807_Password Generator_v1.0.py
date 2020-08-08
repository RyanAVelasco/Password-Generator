import random
import string
# from Tkinter import *

temp = []

alpL = input("lowercase letters?: yes/no")
if alpL == "yes":alpL = True

alpU = input("uppercase letters?: yes/no")
if alpU == "yes":alpU = True

pun = input("punctuations: yes/no")
if pun == "yes":pun = True

numb = input("numbers?: yes/no")
if numb == "yes":numb = True

num = int(input("length of password: "))
gen = 0

while gen < num:
    if alpL is True:
        temp.append(random.choice(string.ascii_lowercase))
    if alpU is True:
        temp.append(random.choice(string.ascii_uppercase))
    if pun is True:
        temp.append(random.choice(string.punctuation))
    if numb is True:
        temp.append(random.choice(string.digits))
    gen += 1

random.shuffle(temp)

for n in temp:
    print(n, end="")