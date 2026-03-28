import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    intentos = [0]

    Label(contenedor, text="4. Validación de número menor que 10", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Ingresa un número entero").pack()
    entry_numero = Entry(contenedor)
    entry_numero.pack()

    resultado = Label(contenedor, text="")
    resultado.pack(pady=5)

    def validar():
        try:
            numero = int(entry_numero.get())
            intentos[0] += 1
        except:
            messagebox.showerror("Error", "Ingresa un entero")
            return

        if numero < 10:
            resultado.config(text=f"Número correcto: {numero} | Intentos: {intentos[0]}")
        else:
            messagebox.showerror("Error", "Debe ser menor que 10")

    Button(contenedor, text="Validar", command=validar).pack(pady=3)