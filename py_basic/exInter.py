get_name = input('Digite seu nome: ')
lenName = len(get_name)
ind = 0
emptyName = ''

while ind < lenName:
    letterName = get_name[ind]
    emptyName += f'*{letterName}'
    ind += 1
letterName += '*'
print(emptyName)