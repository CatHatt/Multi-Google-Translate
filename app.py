# Setup Google Translate
from googletrans import Translator
translator = Translator()

# Setup TKinter
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.geometry('250x500')
window.title('Hello World!')

items = [
    tk.Label(window, text='Input:'),
    tk.Text(window, width=200, height=250),
    ttk.Combobox(window, textvariable=tk.StringVar())
]

for item in items:
    item.pack()

window.mainloop()