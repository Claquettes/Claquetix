import tkinter as tk
from tkinter import ttk
import time
import functions

window = tk.Tk()
window.title("Claquetix")
window.geometry("400x400")


start_button = ttk.Button(window, text="Start", command=functions.launchBrowser)
start_button.grid(row=2, column=2)



window.mainloop()