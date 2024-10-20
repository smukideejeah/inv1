#Programa: Imvestigación de la librería tkinter
#archivo: rmPerson.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Eliminar una persona
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
from tkinter import ttk, messagebox
from utils.person import Person
def default(table: ttk.Treeview):
    selection = table.selection()
    if not selection:
        messagebox.showwarning("Advertencia", "Selecciona una fila para eliminar.")
        return
    
    item = selection[0]
    vals = table.item(item, "values")

    person = Person(vals[2], vals[3], vals[4], vals[0], vals[1])
    person.delete()
    table.delete(item)
    messagebox.showinfo("Éxito", "Datos eliminados correctamente.")