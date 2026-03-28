import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

compras = []

def descuento_mes(mes):
    if mes == "octubre":
        return 0.15
    elif mes == "diciembre":
        return 0.20
    elif mes == "julio":
        return 0.10
    else:
        return 0

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    Label(contenedor, text="3. Sistema de descuentos por mes en tienda", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Nombre del cliente").pack()
    entry_nombre = Entry(contenedor)
    entry_nombre.pack()

    Label(contenedor, text="Mes de la compra").pack()
    entry_mes = Entry(contenedor)
    entry_mes.pack()

    Label(contenedor, text="Importe de compra").pack()
    entry_importe = Entry(contenedor)
    entry_importe.pack()

    resultado = Label(contenedor, text="")
    resultado.pack(pady=5)

    texto = Text(contenedor, width=70, height=10)
    texto.pack(pady=10)

    def registrar():
        nombre = entry_nombre.get()
        mes = entry_mes.get().lower()

        meses_validos = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]

        if nombre == "":
            messagebox.showerror("Error", "Ingresa el nombre")
            return

        if mes not in meses_validos:
            messagebox.showerror("Error", "Mes no válido")
            return

        try:
            importe = float(entry_importe.get())
            if importe <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Importe inválido")
            return

        total = importe - (importe * descuento_mes(mes))
        compras.append([nombre, mes, importe, total])

        resultado.config(text="Total final: " + str(round(total, 2)))

    def mostrar_total():
        texto.delete("1.0", tk.END)
        suma = 0
        for c in compras:
            texto.insert(tk.END, f"{c[0]} | Mes: {c[1]} | Importe: {c[2]} | Total: {round(c[3],2)}\n")
            suma += c[3]
        texto.insert(tk.END, f"\nTotal vendido en el día: {round(suma,2)}")

    Button(contenedor, text="Registrar", command=registrar).pack(pady=3)
    Button(contenedor, text="Mostrar ventas", command=mostrar_total).pack(pady=3)