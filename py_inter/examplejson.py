import json

# people = {
#     "name": "Santiago",
#     "age": 20,
#     "address":[
#         {"street":"street1", "city": "citySP", "number": 24}
#     ]
# }

# with open('examplejson.json', 'w', encoding='utf8') as file: #criando arquivo json
#     json.dump(
#         people, 
#         file, 
#         ensure_ascii=False, 
#         indent=2
#         ) #passando as inf que esse arquivo vai ter, selecionando os dados e ação



with open('.\examplejson.json', 'r', encoding='utf8') as file:
    peoples = json.load(file)
    print(peoples)
