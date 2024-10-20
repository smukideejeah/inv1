#Programa: Imvestigación de la librería tkinter
#archivo: table.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Crear una tabla con los datos de las personas
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
from tkinter import ttk, messagebox

from utils.persons import default as persons
from events.setDataEntry import default as setDataEntry

def default(window: ttk, datas: list):
    table = ttk.Treeview(window, columns=("Cédula", "Tipo", "Nombre", "Edad", "Provincia"), show="headings")

    table.heading("Cédula", text="Cédula")
    table.heading("Tipo", text="Tipo")
    table.heading("Nombre", text="Nombre")
    table.heading("Edad", text="Edad")
    table.heading("Provincia", text="Provincia")

    table.column("Cédula", width=100)
    table.column("Tipo", width=50)
    table.column("Nombre", width=100)
    table.column("Edad", width=30)
    table.column("Provincia", width=100)


    table.bind("<Double-1>", lambda e: setDataEntry(datas[0], datas[1], datas[2], datas[3], datas[4], table))

    # Leer los datos desde el archivo JSON y llenar la tabla
    init = persons()

    if(init == None):
        return table

    for person in init:
        table.insert("", "end", values=(person.id, person.typeId, person.name, person.age, person.province))

    table.pack(pady=10, padx=10, fill="both", expand=True)
    return table 
