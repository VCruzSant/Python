import json

from class_in_JSON_post import PATH_FILE, People


with open(PATH_FILE, 'r', encoding='utf8') as file:
    data = json.load(file)

    p1 = People(**data[0])
    p2 = People(**data[1])
    p3 = People(**data[2])

    print(p1.name)
    print(p2.name)
    print(p3.name)
