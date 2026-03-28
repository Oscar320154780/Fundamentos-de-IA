import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

trabajadores = []

def calcular_pago(hn, ph, he, hijos):
    pago_normal = hn * ph
    pago_extra = he * (ph * 1.5)
    bonificacion = hijos * 0.5
    total = pago_normal + pago_extra + bonificacion
    return pago_normal, pago_extra, bonificacion, total

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    Label(contenedor, text="10. Sistema de pago de trabajadores", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Nombre del trabajador").pack()
    entry_nombre = Entry(contenedor)
    entry_nombre.pack()

    Label(contenedor, text="Horas normales trabajadas").pack()
    entry_hn = Entry(contenedor)
    entry_hn.pack()

    Label(contenedor, text="Pago por hora normal").pack()
    entry_ph = Entry(contenedor)
    entry_ph.pack()

    Label(contenedor, text="Horas extras trabajadas").pack()
    entry_he = Entry(contenedor)
    entry_he.pack()

    Label(contenedor, text="Número de hijos").pack()
    entry_hijos = Entry(contenedor)
    entry_hijos.pack()

    resultado = Label(contenedor, text="")
    resultado.pack(pady=5)

    texto = Text(contenedor, width=75, height=10)
    texto.pack(pady=10)

    def registrar():
        nombre = entry_nombre.get()

        if nombre == "":
            messagebox.showerror("Error", "Ingresa el nombre")
            return

        try:
            hn = float(entry_hn.get())
            ph = float(entry_ph.get())
            he = float(entry_he.get())
            hijos = int(entry_hijos.get())

            if hn < 0 or ph <= 0 or he < 0 or hijos < 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Datos inválidos")
            return

        normal, extra, bono, total = calcular_pago(hn, ph, he, hijos)

        trabajadores.append([nombre, normal, extra, bono, total])

        resultado.config(text="Pago total: " + str(round(total, 2)))

    def mostrar_reporte():
        texto.delete("1.0", tk.END)
        for t in trabajadores:
            texto.insert(
                tk.END,
                f"{t[0]} | Pago normal: {round(t[1],2)} | Pago extra: {round(t[2],2)} | Bono: {round(t[3],2)} | Total: {round(t[4],2)}\n"
            )

    Button(contenedor, text="Registrar", command=registrar).pack(pady=3)
    Button(contenedor, text="Mostrar reporte", command=mostrar_reporte).pack(pady=3)