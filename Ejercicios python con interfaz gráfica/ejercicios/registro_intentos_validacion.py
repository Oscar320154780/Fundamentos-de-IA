import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

intentos = []

def numero_valido(n):
    return n > 0 and n < 20

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    Label(contenedor, text="6. Registro de intentos de validación", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Ingresa un número entero").pack()
    entry_numero = Entry(contenedor)
    entry_numero.pack()

    resultado = Label(contenedor, text="")
    resultado.pack(pady=5)

    texto = Text(contenedor, width=70, height=10)
    texto.pack(pady=10)

    def registrar():
        try:
            numero = int(entry_numero.get())
        except:
            messagebox.showerror("Error", "Ingresa un entero")
            return

        intentos.append(numero)

        if numero_valido(numero):
            incorrectos = 0
            for n in intentos:
                if not numero_valido(n):
                    incorrectos += 1
            resultado.config(text=f"Número correcto: {numero} | Incorrectos: {incorrectos}")
        else:
            messagebox.showerror("Error", "Número fuera del rango")

    def mostrar_historial():
        texto.delete("1.0", tk.END)
        incorrectos = 0
        for n in intentos:
            texto.insert(tk.END, str(n) + "\n")
            if not numero_valido(n):
                incorrectos += 1
        texto.insert(tk.END, "\nIntentos incorrectos: " + str(incorrectos))

    Button(contenedor, text="Registrar", command=registrar).pack(pady=3)
    Button(contenedor, text="Mostrar historial", command=mostrar_historial).pack(pady=3)