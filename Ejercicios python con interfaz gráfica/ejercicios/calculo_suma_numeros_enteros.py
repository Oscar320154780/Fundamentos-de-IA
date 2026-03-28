import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

def suma_n(n):
    suma = 0
    lista = []
    for i in range(1, n + 1):
        suma += i
        lista.append(i)
    return lista, suma

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    Label(contenedor, text="7. Cálculo de suma de números enteros", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Ingresa n").pack()
    entry_n = Entry(contenedor)
    entry_n.pack()

    texto = Text(contenedor, width=70, height=10)
    texto.pack(pady=10)

    def calcular():
        try:
            n = int(entry_n.get())
            if n <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Ingresa un número positivo")
            return

        lista, suma = suma_n(n)
        texto.delete("1.0", tk.END)
        texto.insert(tk.END, "Secuencia: " + str(lista))
        texto.insert(tk.END, "\nResultado final: " + str(suma))

    Button(contenedor, text="Calcular", command=calcular).pack(pady=3)