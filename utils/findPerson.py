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
    
    
    
    
