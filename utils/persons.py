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
    
    
    
    
