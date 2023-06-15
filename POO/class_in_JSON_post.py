import json
PATH_FILE = '.\\POO\\class_in_JSON.json'

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = People('vini', 19)
p2 = People('Cruz', 20)
p3 = People('Santiago', 21)

bd = [p1.__dict__, vars(p2), p3.__dict__]

def make_dump():
    with open(PATH_FILE, 'w', encoding='utf8') as file:
        print('fiz dump')
        json.dump(bd, file, ensure_ascii=False, indent=2)
    

if __name__ == '__main__':
    print('ele é o __main__')
    make_dump()