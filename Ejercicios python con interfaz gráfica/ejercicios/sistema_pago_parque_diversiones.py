import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

visitantes = []

def calcular_descuento(edad):
    if edad < 10:
        return 0.25
    elif edad <= 17:
        return 0.10
    else:
        return 0

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    Label(contenedor, text="2. Sistema de pago en parque de diversiones", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Nombre").pack()
    entry_nombre = Entry(contenedor)
    entry_nombre.pack()

    Label(contenedor, text="Edad").pack()
    entry_edad = Entry(contenedor)
    entry_edad.pack()

    Label(contenedor, text="Cantidad de juegos utilizados").pack()
    entry_juegos = Entry(contenedor)
    entry_juegos.pack()

    resultado = Label(contenedor, text="")
    resultado.pack(pady=5)

    texto = Text(contenedor, width=70, height=10)
    texto.pack(pady=10)

    def registrar():
        nombre = entry_nombre.get()

        if nombre == "":
            messagebox.showerror("Error", "Ingresa el nombre")
            return

        try:
            edad = int(entry_edad.get())
            juegos = int(entry_juegos.get())
            if edad < 0 or juegos < 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Datos inválidos")
            return

        total = juegos * 50
        descuento = total * calcular_descuento(edad)
        pagar = total - descuento

        visitantes.append([nombre, edad, juegos, pagar])

        resultado.config(text="Total a pagar: " + str(round(pagar, 2)))

    def mostrar_recaudado():
        texto.delete("1.0", tk.END)
        total = 0
        for v in visitantes:
            texto.insert(tk.END, f"{v[0]} | Edad: {v[1]} | Juegos: {v[2]} | Pago: {round(v[3],2)}\n")
            total += v[3]
        texto.insert(tk.END, f"\nTotal recaudado: {round(total,2)}")

    Button(contenedor, text="Registrar", command=registrar).pack(pady=3)
    Button(contenedor, text="Mostrar total recaudado", command=mostrar_recaudado).pack(pady=3)