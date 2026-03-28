import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    numeros = []

    Label(contenedor, text="8. Sistema de suma acumulativa", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Ingresa números, 0 para terminar").pack()
    entry_numero = Entry(contenedor)
    entry_numero.pack()

    resultado = Label(contenedor, text="Suma acumulada: 0")
    resultado.pack(pady=5)

    texto = Text(contenedor, width=70, height=10)
    texto.pack(pady=10)

    def agregar():
        try:
            numero = int(entry_numero.get())
        except:
            messagebox.showerror("Error", "Ingresa un entero")
            return

        if numero == 0:
            texto.delete("1.0", tk.END)
            texto.insert(tk.END, "Lista de números ingresados: " + str(numeros))
            texto.insert(tk.END, "\nCantidad de números: " + str(len(numeros)))
            texto.insert(tk.END, "\nSuma total: " + str(sum(numeros)))
        else:
            numeros.append(numero)
            resultado.config(text="Suma acumulada: " + str(sum(numeros)))

    Button(contenedor, text="Agregar", command=agregar).pack(pady=3)