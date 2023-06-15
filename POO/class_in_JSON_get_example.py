import json

from class_in_JSON_post_example import PATH_FILE, Car

with open(PATH_FILE, 'r', encoding='utf8') as file:
    data = json.load(file)
    
    c1 = Car(**data[0])
    c2 = Car(**data[1])
    c3 = Car(**data[2])

    print(c1.name)
    print(c2.name)
    print(c3.name)