import json

PATH_FILE = '.\\POO\\class_in_JSON_example.json'

class Car:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

c1 = Car('dodge', 'charger')
c2 = Car('bmw', '218i')
c3 = Car('meca', 'GLA')

bd = [c1.__dict__, vars(c2), c3.__dict__]

def make_dump():
    with open(PATH_FILE, 'w+', encoding='utf8') as file:
        print('fiz dump')
        json.dump(bd, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('esse é o __main__ ent posso fazer o dump')
    make_dump()