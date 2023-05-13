import tkinter as tk
from tkinter import ttk
import time
import functions as f
def start(nb):
    f.launchBrowser(nb)
    print("On a choisi de tester " + nb.get() + " mots")
    print("On lance le test")

window = tk.Tk()
window.title("Claquetix")
window.geometry("400x400")

nb = tk.IntVar()
nb_menu = ttk.OptionMenu(window, nb, 1000, 100, 1000, 10000, 600000)
nb_menu.grid(row=2, column=1)

start_button = ttk.Button(window, text="Start", command=lambda: start(nb.get()))
start_button.grid(row=2, column=2)
window.mainloop()

