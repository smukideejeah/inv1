#Programa: Imvestigación de la librería tkinter
#archivo: setDataEntry.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Establecer los valores de una persona en el formulario para editar
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
from tkinter import ttk, Entry

def default(id: Entry, typeId: ttk.Combobox, name: Entry, age: Entry, province: ttk.Combobox, table: ttk.Treeview):
    selection = table.selection()
    item = selection[0]
    vals = table.item(item, "values")

    from utils.person import Person
    person = Person(vals[2], vals[3], vals[4], vals[0], vals[1])
    id.delete(0, "end")
    id.insert(0, person.id)
    typeId.set(person.typeId)
    name.delete(0, "end")
    name.insert(0, person.name)
    age.delete(0, "end")
    age.insert(0, person.age)
    province.set(person.province)
