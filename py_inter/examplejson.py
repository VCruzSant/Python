import json
import os

people_my = {
    "name": 'Santiago',
    "age": 20,
    "address":[
        {"street":'Tiberio', "city": 'Cotia'}
    ]
}

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'examplejson.json')

with open(SAVE_TO, 'w', encoding='utf8') as file:
    json.dump(people_my, file, indent=2) #-> jogar pra fora
    file.seek(0, 0)

with open(SAVE_TO, 'r') as file:
    peoples = json.load(file)
    
    for people in peoples:
        print(peoples['name'])

