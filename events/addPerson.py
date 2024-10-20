#Programa: Imvestigación de la librería tkinter
#archivo: addPerson.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Guardar o actualizar una persona
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
from tkinter import ttk, messagebox
from utils.person import Person
def default(name: str, age: int, province: str, id: str, typeId: str, table: ttk.Treeview, datas: list):
    person = Person(name, age, province, id, typeId)
    append = person.upsert()

    if(append):
        table.insert("", "end", values=(id, typeId, name, age, province))
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    else:
        children = table.get_children()
        for child in children:
            values = table.item(child, "values")
            if(values[0] == id):
                table.item(child, values=(id, typeId, name, age, province))
                break

        messagebox.showinfo("Éxito", "Datos actualizados correctamente.")

    datas[0].delete(0, "end")
    datas[1].set("")
    datas[2].delete(0, "end")
    datas[3].delete(0, "end")
    datas[4].set("")