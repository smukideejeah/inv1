import json
from typing import List
from utils.person import Person
from conf.env import ROUTEPERSON

def default(province: str) -> List[Person]:
    with open(ROUTEPERSON, 'r', encoding="utf8") as file:
        data = json.load(file)
    
    personData = list(filter(lambda person: person['province'] == province, data))
    persons: List[Person] = []
    
    for person in personData:
        persons.append(Person(person['name'], person['age'], person['province'], person['id'], person['typeId']))
    
    return persons
    
    
    
    
