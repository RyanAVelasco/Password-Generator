import random
import string
# from Tkinter import *

alphabet_lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

alphabet_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                      "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbol = ['!', '"', '#', '$', '%', '&', ',', '(',
               ')', '*', '+', '-', '.', '/', ':', ';',
               '<', '=', '>', '?', '@', '[', '\\', ']',
               '^', '`', '{', '|', '}', '~']

password_container = list()

choice_lower = input("lowercase letters?: yes/no").lower().strip()
if choice_lower == "yes" : choice_lower = True


choice_uppercase = input("uppercase letters?: yes/no").lower().strip()
if choice_uppercase == "yes" : choice_uppercase = True


choice_digit = input("numbers?: yes/no").strip()
if choice_digit == "yes" : choice_digit = True


choice_symbol = input("symbols?: yes/no").strip()
if choice_symbol == "yes" : choice_symbol = True

password_length = int(input("length of password: ").strip())
iteration = 0

while iteration != password_length:
    if choice_lower is True:
        password_container.append(random.choice(alphabet_lowercase))
    if choice_uppercase is True:
        password_container.append(random.choice(alphabet_uppercase))
    if choice_digit is True:
        password_container.append(random.choice(digit))
    if choice_symbol is True:
        password_container.append(random.choice(symbol))
    iteration += 1

random.shuffle(password_container)

for n in password_container:
    print(n, end="")