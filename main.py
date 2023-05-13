import tkinter as tk
from tkinter import ttk
import time
import functions as f

nb = 1000
def start(nb):
    f.launchBrowser(nb)
    print("done")

window = tk.Tk()
window.title("Claquetix")
window.geometry("400x400")

start_button = ttk.Button(window, text="Start", command=lambda: start(nb))
start_button.grid(row=2, column=2)

##on ajoute un menu déroulant, pour choisir le nombre de mots à tester
nb_label = ttk.Label(window, text="Nombre de mots à tester :")
nb_label.grid(row=1, column=1)
nb = 1000
##on met un bouton radio pour chaque nombre de mots
nb_100 = ttk.Radiobutton(window, text="100", variable=nb, value=100)
nb_100.grid(row=2, column=1)
nb_1000 = ttk.Radiobutton(window, text="1000", variable=nb, value=1000)
nb_1000.grid(row=3, column=1)
nb_10000 = ttk.Radiobutton(window, text="10000", variable=nb, value=10000)
nb_10000.grid(row=4, column=1)
nb_600000 = ttk.Radiobutton(window, text="600000", variable=nb, value=600000)
nb_600000.grid(row=5, column=1)
infini = ttk.Radiobutton(window, text="infini", variable=nb, value=0)
infini.grid(row=6, column=1)
print(nb)

window.mainloop()

