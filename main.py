import tkinter as tk
from tkinter import ttk
import time
import functions

nb = 1000

window = tk.Tk()
window.title("Claquetix")
window.geometry("400x400")




start_button = ttk.Button(window, text="Start", command=functions.launchBrowser(nb))
start_button.grid(row=2, column=2)

##on ajoute un menu déroulant, pour choisir le nombre de mots à tester
nb_label = ttk.Label(window, text="Nombre de mots à tester :")
nb_label.grid(row=1, column=1)
nb = tk.StringVar()
nb.set("10")
nb_menu = ttk.OptionMenu(window, nb, "100", "1000", "10000", "600000")
nb_menu.grid(row=1, column=2)






window.mainloop()