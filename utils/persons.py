#Programa: Imvestigación de la librería tkinter
#archivo: persons.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Obtener todas las personas almacenadas en el archivo json
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
import json
from typing import List
from utils.person import Person
from conf.env import ROUTEPERSON

def default() -> List[Person] | None:
    persons: List[Person] = []
    with open(ROUTEPERSON, 'r', encoding="utf8") as file:
        personData = json.load(file)

    for person in personData:
        persons.append(Person(person['name'], person['age'], person['province'], person['id'], person['typeId']))
    
    return persons
    
    
    
    
