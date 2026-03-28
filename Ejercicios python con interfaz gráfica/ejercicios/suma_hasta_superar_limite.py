import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox

def mostrar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    numeros = []
    suma = 0
    terminado = [False]  

    Label(contenedor, text="9. Suma de números hasta superar un límite", font=("Arial", 14)).pack(pady=10)

    Label(contenedor, text="Ingresa números enteros").pack()
    entry_numero = Entry(contenedor)
    entry_numero.pack()

    resultado = Label(contenedor, text="Suma parcial: 0")
    resultado.pack(pady=5)

    texto = Text(contenedor, width=70, height=10)
    texto.pack(pady=10)

    def agregar():
        nonlocal suma

        if terminado[0]:
            messagebox.showinfo("Info", "Ya se alcanzo el límite")
            return

        try:
            numero = int(entry_numero.get())
        except:
            messagebox.showerror("Error", "Ingresa un numero entero")
            return

        numeros.append(numero)
        suma += numero

        resultado.config(text="Suma parcial: " + str(suma))

        entry_numero.delete(0, tk.END)

        if suma > 100:
            terminado[0] = True

            texto.delete("1.0", tk.END)
            texto.insert(tk.END, "Cantidad de números ingresados: " + str(len(numeros)))
            texto.insert(tk.END, "\nLista de números: " + str(numeros))
            texto.insert(tk.END, "\nSuma final: " + str(suma))

            messagebox.showinfo("Finalizado", "La suma supero 100")

    Button(contenedor, text="Agregar", command=agregar).pack(pady=3)