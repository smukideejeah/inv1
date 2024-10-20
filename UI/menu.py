#Programa: Imvestigación de la librería tkinter
#archivo: menu.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Creación de un menú para buscar por provincia
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
from tkinter import ttk, Menu
from conf.env import PROVINCES
from UI.searchByProvince import default as searchByProvince

def default(window: ttk):
    menu = Menu(window)
    window.config(menu=menu)

    provincesMenu = Menu(menu, tearoff=0)

    for province in PROVINCES:
        provincesMenu.add_command(label=province, command=lambda p = province: searchByProvince(window, p))

    menu.add_cascade(label="Buscar por Provincia", menu=provincesMenu)