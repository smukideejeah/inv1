#Programa: Imvestigación de la librería tkinter
#archivo: person.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Crear, actualizar y eliminar una persona utilizando una clase
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
import json
from conf.env import ROUTEPERSON

class Person:
    def __init__(self, name: str, age: int, province: str, id: str, typeId: str):
        self.name: str = name
        self.age: int = age
        self.province: str = province
        self.id: str = id
        self.typeId: str = typeId

    def upsert(self):
        with open(ROUTEPERSON, "r", encoding="utf8") as file:
            personsData = json.load(file)
        
        new = list(filter(lambda person: person['id'] == self.id, personsData))
        append = False
        if(len(new) == 0):
            personsData.append({
                "name": self.name,
                "age": self.age,
                "province": self.province,
                "id": self.id,
                "typeId": self.typeId
            })
            append = True
        else:
            personsDataIndex = personsData.index(new[0])
            personsData[personsDataIndex] = {
                "name": self.name,
                "age": self.age,
                "province": self.province,
                "id": self.id,
                "typeId": self.typeId
            }
        
        with open(ROUTEPERSON, "w", encoding="utf8") as file:
            json.dump(personsData, file, indent=4, ensure_ascii=False)

        return append

    def delete(self):
        with open(ROUTEPERSON, "r", encoding="utf8") as file:
            personsData = json.load(file)
        
        new = list(filter(lambda person: person['id'] == self.id, personsData))

        if(len(new) == 0):
            return False
        
        personsData.remove(new[0])

        with open(ROUTEPERSON, "w", encoding="utf8") as file:
            json.dump(personsData, file, indent=4, ensure_ascii=False)
            return True