#Programa: Imvestigación de la librería tkinter
#archivo: form.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Crear un formulario para ingresar datos personales
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
import tkinter as tk
from tkinter import ttk
from UI.table import default as initTable
from conf.env import PROVINCES
from events.addPerson import default as addPerson
from events.rmPerson import default as rmPerson
from UI.menu import default as initMenu

# Configuración de la ventana principal
def createForm():
    window = tk.Tk()
    window.title("Registro Civil")
    window.geometry("800x600")

    initMenu(window)



    frameTable = tk.Frame(window)
    frameTable.pack(pady=10)

    tk.Label(frameTable, text="Cédula").grid(row=0, column=0, padx=5, pady=5)
    id = tk.Entry(frameTable)
    id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frameTable, text="Tipo").grid(row=1, column=0, padx=5, pady=5)
    typeId = ttk.Combobox(frameTable, values=["Nacional", "DIMEX", "Pasaporte"], state="readonly")	
    typeId.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frameTable, text="Nombre").grid(row=2, column=0, padx=5, pady=5)
    name = tk.Entry(frameTable)
    name.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frameTable, text="Edad").grid(row=3, column=0, padx=5, pady=5)
    age = tk.Entry(frameTable)
    age.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frameTable, text="Provincia").grid(row=4, column=0, padx=5, pady=5)
    province = ttk.Combobox(frameTable, values=PROVINCES, state="readonly")
    province.grid(row=4, column=1, padx=5, pady=5)


    # Crear un Frame para los botones
    frameButtons = tk.Frame(window)
    frameButtons.pack(pady=10)

    # Botón para agregar datos
    add = tk.Button(
        frameButtons,
        text="Agregar",
        command=lambda: addPerson(name.get(), age.get(), province.get(), id.get(), typeId.get(), table, [id, typeId, name, age, province])
    )
    add.pack(side=tk.LEFT, padx=5)

    _del = tk.Button(
        frameButtons,
        text="Eliminar",
        command=lambda: rmPerson(table)
    )
    _del.pack(side=tk.LEFT, padx=5)  

    table = initTable(window, [id, typeId, name, age, province])


    window.mainloop()
