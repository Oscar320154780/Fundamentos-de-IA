import customtkinter as ctk
from tkinter import messagebox
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ARCHIVO = "usuarios.txt"

# Si no existe el archivo, lo crea con usuarios de prueba
if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write("admin,1234\n")
        f.write("alumno,1111\n")


def validar_usuario(usuario, contrasena):
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(",")

            if len(datos) == 2:
                user = datos[0]
                password = datos[1]

                if usuario == user and contrasena == password:
                    return True

    return False


datos = [
    ["Luis", "6IM7", 8.5, "Programacion", "Aprobado"],
    ["Ana", "6IM8", 9.4, "Base de Datos", "Aprobado"],
    ["Carlos", "6IM7", 5.8, "Fisica", "Reprobado"],
    ["Maria", "6IM9", 7.2, "Quimica", "Aprobado"],
    ["Pedro", "6IM8", 6.1, "Programacion", "Reprobado"],
    ["Sofia", "6IM7", 9.8, "Base de Datos", "Aprobado"],
    ["Diego", "6IM9", 8.0, "Fisica", "Aprobado"],
    ["Valeria", "6IM8", 9.1, "Programacion", "Aprobado"],
    ["Jorge", "6IM7", 6.5, "Quimica", "Reprobado"],
    ["Fernanda", "6IM9", 10.0, "Base de Datos", "Aprobado"],
]


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Consultas")
        self.geometry("800x500")

        self.login()

    def limpiar(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login(self):
        self.limpiar()

        frame = ctk.CTkFrame(self)
        frame.pack(pady=80)

        ctk.CTkLabel(frame, text="Inicio de sesion", font=("Arial", 22)).pack(pady=15)

        self.usuario = ctk.CTkEntry(frame, placeholder_text="Usuario")
        self.usuario.pack(padx=40, pady=10)

        self.contrasena = ctk.CTkEntry(frame, placeholder_text="Contraseña", show="*")
        self.contrasena.pack(padx=40, pady=10)

        ctk.CTkButton(frame, text="Entrar", command=self.entrar).pack(pady=20)

    def entrar(self):
        user = self.usuario.get()
        password = self.contrasena.get()

        if user == "" or password == "":
            messagebox.showwarning("Aviso", "Llena todos los campos")
        elif validar_usuario(user, password):
            self.menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def menu(self):
        self.limpiar()

        frame_botones = ctk.CTkFrame(self)
        frame_botones.pack(side="left", fill="y", padx=10, pady=10)

        self.frame_resultado = ctk.CTkFrame(self)
        self.frame_resultado.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(frame_botones, text="Consultas", font=("Arial", 20)).pack(pady=10)

        consultas = [
            ("1. Todos los alumnos", lambda: self.consulta(datos)),
            ("2. Aprobados", lambda: self.consulta([x for x in datos if x[4] == "Aprobado"])),
            ("3. Reprobados", lambda: self.consulta([x for x in datos if x[4] == "Reprobado"])),
            ("4. Promedio mayor a 9", lambda: self.consulta([x for x in datos if x[2] > 9])),
            ("5. Promedio menor a 7", lambda: self.consulta([x for x in datos if x[2] < 7])),
            ("6. Grupo 6IM7", lambda: self.consulta([x for x in datos if x[1] == "6IM7"])),
            ("7. Grupo 6IM8", lambda: self.consulta([x for x in datos if x[1] == "6IM8"])),
            ("8. Programacion aprobados", lambda: self.consulta([x for x in datos if x[3] == "Programacion" and x[4] == "Aprobado"])),
            ("9. Base de Datos", lambda: self.consulta([x for x in datos if x[3] == "Base de Datos"])),
            ("10. Mejor promedio", lambda: self.consulta([max(datos, key=lambda x: x[2])])),
        ]

        for texto, accion in consultas:
            ctk.CTkButton(frame_botones, text=texto, width=210, command=accion).pack(pady=5)

        ctk.CTkButton(frame_botones, text="Salir", command=self.login).pack(pady=20)

        self.consulta([])

    def consulta(self, resultado):
        for widget in self.frame_resultado.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.frame_resultado, text="Resultados", font=("Arial", 20)).pack(pady=10)

        texto = ctk.CTkTextbox(self.frame_resultado, width=480, height=380)
        texto.pack(padx=10, pady=10)

        if len(resultado) == 0:
            texto.insert("end", "Selecciona una consulta.")
        else:
            texto.insert("end", "Nombre\tGrupo\tPromedio\tMateria\t\tEstado\n")
            texto.insert("end", "-" * 65 + "\n")

            for alumno in resultado:
                texto.insert(
                    "end",
                    f"{alumno[0]}\t{alumno[1]}\t{alumno[2]}\t\t{alumno[3]}\t\t{alumno[4]}\n"
                )

        texto.configure(state="disabled")


app = App()
app.mainloop()
