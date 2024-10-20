#Programa: Imvestigación de la librería tkinter
#archivo: searchByProvince.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Ventana que obtiene los registros de una provincia
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from UI.provinceTable import default as initTable
from utils.findByProvince import default as findByProvince

def default(main: tk, province: str):
    init = findByProvince(province)

    if(len(init) == 0):
        messagebox.showwarning("Advertencia", f"No hay registros en la provincia de {province}")
        return

    window = tk.Toplevel(main)
    window.title(f"Registro de {province}")
    window.geometry("800x400")

    table = initTable(window, init)

    frameTable = tk.Frame(window)
    frameTable.pack(pady=10)
