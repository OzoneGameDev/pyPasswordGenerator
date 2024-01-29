import secrets
import string
import tkinter as tk
from tkinter import ttk

alphabet = string.ascii_letters + string.digits + string.punctuation


def generate():
    length = int(lengthInput.get())
    if length < 4:
        length = 4
    elif length > 100:
        length = 100
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    generatedPassword.set(password)
    print(password)



window = tk.Tk()
window.title("Password Generator")
window.config(width=600)
window.resizable(width=False, height=False)

defaultValue = tk.IntVar(window, value=8)
generatedPassword = tk.StringVar(window, value="Your password will be shown here")

title = ttk.Label(window, text="Python Password Generator", font=("",25))
title.pack(pady=10)

options = ttk.Frame(window)
options.pack(pady=10)

lengthText = ttk.Label(options, text="Length: ")
lengthText.pack(side="left")

lengthInput = ttk.Spinbox(options, from_=4, to=100, textvariable=defaultValue)
lengthInput.pack()

generateButton = ttk.Button(window, text="Generate!", command=generate)
generateButton.pack(pady=10)

generatedText = ttk.Entry(window, textvariable=generatedPassword, width=100)
generatedText.pack(pady=10, padx=20)

window.mainloop()
