from tkinter import *
import random

secret = random.randint(1, 100)

def check_guess():
    guess = int(number.get())
    if guess == secret:
        result.config(text="félicitations!")
    elif guess < secret:
        result.config(text="Essayez un nombre plus élevé.")
    else:
        result.config(text="Essayez un nombre inférieur.")

window = Tk()
window.title("Guess the Number")

Label(window, text="Guess the number (1-100):").pack()
number = Entry(window)
number.pack()

Button(window, text="Check Guess", command=check_guess).pack()

result = Label(window, text="")
result.pack()

window.mainloop()
