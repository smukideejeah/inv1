#Programa: Imvestigación de la librería tkinter
#archivo: findPerson.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Buscar una persona por su id
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
import json
from utils.person import Person
from conf.env import ROUTEPERSON

def findPerson(id) -> Person | None:
    with open(ROUTEPERSON, 'r', encoding="utf8") as file:
        data = json.load(file)
    
    personData = list(filter(lambda person: person['id'] == id, data))
    if(len(personData) == 0):
        return None
    
    personData = personData[0]
    return Person(personData['name'], personData['age'], personData['province'], personData['id'], personData['typeId'])
    
    
    
    
