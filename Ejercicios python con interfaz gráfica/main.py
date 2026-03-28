import tkinter as tk
from tkinter import Button, Label, Frame

from ejercicios import sistema_aumento_sueldos
from ejercicios import sistema_pago_parque_diversiones
from ejercicios import sistema_descuentos_mes_tienda
from ejercicios import validacion_numero_menor_10
from ejercicios import validacion_numero_rango_0_20
from ejercicios import registro_intentos_validacion
from ejercicios import calculo_suma_numeros_enteros
from ejercicios import sistema_suma_acumulativa
from ejercicios import suma_hasta_superar_limite
from ejercicios import sistema_pago_trabajadores


ventana = tk.Tk()
ventana.title("Menu principal")
ventana.geometry("950x650")


def limpiar(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()


menu = Frame(ventana)
menu.pack(side="left", fill="y", padx=10, pady=10)

contenedor = Frame(ventana)
contenedor.pack(side="right", fill="both", expand=True, padx=10, pady=10)

Label(menu, text="MENU PRINCIPAL", font=("Arial", 14, "bold")).pack(pady=10)

Button(menu, text="1. Aumento de sueldos", width=28,
       command=lambda: sistema_aumento_sueldos.mostrar(contenedor)).pack(pady=3)

Button(menu, text="2. Pago parque", width=28,
       command=lambda: sistema_pago_parque_diversiones.mostrar(contenedor)).pack(pady=3)

Button(menu, text="3. Descuentos tienda", width=28,
       command=lambda: sistema_descuentos_mes_tienda.mostrar(contenedor)).pack(pady=3)

Button(menu, text="4. Menor que 10", width=28,
       command=lambda: validacion_numero_menor_10.mostrar(contenedor)).pack(pady=3)

Button(menu, text="5. Rango (0,20)", width=28,
       command=lambda: validacion_numero_rango_0_20.mostrar(contenedor)).pack(pady=3)

Button(menu, text="6. Registro de intentos", width=28,
       command=lambda: registro_intentos_validacion.mostrar(contenedor)).pack(pady=3)

Button(menu, text="7. Suma de enteros", width=28,
       command=lambda: calculo_suma_numeros_enteros.mostrar(contenedor)).pack(pady=3)

Button(menu, text="8. Suma acumulativa", width=28,
       command=lambda: sistema_suma_acumulativa.mostrar(contenedor)).pack(pady=3)

Button(menu, text="9. Suma hasta superar 100", width=28,
       command=lambda: suma_hasta_superar_limite.mostrar(contenedor)).pack(pady=3)

Button(menu, text="10. Pago trabajadores", width=28,
       command=lambda: sistema_pago_trabajadores.mostrar(contenedor)).pack(pady=3)

Button(menu, text="Salir", width=28, command=ventana.destroy).pack(pady=20)

Label(contenedor, text="Selecciona un ejercicio del menu", font=("Arial", 14)).pack(pady=20)

ventana.mainloop()