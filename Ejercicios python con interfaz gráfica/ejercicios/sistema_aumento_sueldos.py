import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

trabajadores = []

def calcular_aumento(sueldo):
    if sueldo < 4000:
        return sueldo * 0.15
    elif sueldo <= 7000:
        return sueldo * 0.10
    else:
        return sueldo * 0.08

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    Label(contenedor, text="1. Sistema de aumento de sueldos", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Nombre del trabajador").pack()
    entry_nombre = Entry(contenedor)
    entry_nombre.pack()

    Label(contenedor, text="Sueldo básico").pack()
    entry_sueldo = Entry(contenedor)
    entry_sueldo.pack()

    resultado = Label(contenedor, text="")
    resultado.pack(pady=5)

    texto = Text(contenedor, width=70, height=10)
    texto.pack(pady=10)

    def registrar():
        nombre = entry_nombre.get()
        sueldo_txt = entry_sueldo.get()

        if nombre == "":
            messagebox.showerror("Error", "Ingresa el nombre")
            return

        try:
            sueldo = float(sueldo_txt)
            if sueldo <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Ingresa un sueldo válido")
            return

        aumento = calcular_aumento(sueldo)
        nuevo = sueldo + aumento

        trabajadores.append([nombre, sueldo, nuevo])

        resultado.config(text="Nuevo sueldo: " + str(round(nuevo, 2)))

        entry_nombre.delete(0, tk.END)
        entry_sueldo.delete(0, tk.END)

    def mostrar_historial():
        texto.delete("1.0", tk.END)
        for t in trabajadores:
            texto.insert(tk.END, f"Nombre: {t[0]} | Sueldo: {t[1]} | Nuevo sueldo: {round(t[2],2)}\n")

    Button(contenedor, text="Registrar", command=registrar).pack(pady=3)
    Button(contenedor, text="Mostrar historial", command=mostrar_historial).pack(pady=3)