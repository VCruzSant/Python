people = {}

people['name'] = 'vini'
print(people)

if people.get('sobrenome'): #se usar o if seco, ele vai brecar e não vai aparecer, se usar o .get, é possível fazer esse tipo de lógica
#pode ser usado is none tmb 
    print('existe')
else:
    print('não existe')