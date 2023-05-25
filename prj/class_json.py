import json

# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

PATH_FILE = 'classjson.json'

class People:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def apresentation(self):
        print(f"my name is {self.name}, i'm {self.age} years old and have {self.height} of height")
        return


p1 = People('vini', 20, 1.85)
p2 = People('sant', 20, 1.85)
p3 = People('cruz', 20, 1.85)
bd = [p1.__dict__, p2.__dict__, p3.__dict__]

SAVE_OBJ = bd


def post_json():
    with open(PATH_FILE, 'w', encoding='utf8') as file:
        save_class = json.dump(
            SAVE_OBJ,
            file,
            ensure_ascii=False,
            indent=2
    )
        return save_class


if __name__ == '__main__':
    post_json()
    print("executei o dump")