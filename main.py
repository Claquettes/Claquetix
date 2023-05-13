import tkinter as tk
from tkinter import ttk
import time

import src.functions as f

def start(nb):
    print("On lance le test")
    f.launchBrowser(nb)
    print("On a choisi de tester " + nb.get() + " mots")
    print("On lance le test")

def stop():
    print("Stop testing")
    f.stop()
    window.quit()
    


window = tk.Tk()
window.title("Claquetix")
window.geometry("500x50")

nb = tk.IntVar()
nb_menu = ttk.OptionMenu(window, nb, 1000, 100, 1000, 10000, 600000)
start_button = ttk.Button(window, text="Start", command=lambda: start(nb.get()))
label = ttk.Label(window, text="Choisissez le nombre de mots à tester")
stop_button = ttk.Button(window, text="Stop", command=lambda: stop())

label.grid(row=2, column=1)
nb_menu.grid(row=2, column=2)
start_button.grid(row=2, column=3)
stop_button.grid(row=2, column=4)
window.mainloop()
