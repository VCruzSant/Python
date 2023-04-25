import copy
#para fazer deep copy

d1 = {
    'c1':1,
    'c2':2,
    'l1': [0,1,2],
}

d2 = d1.copy()
d2['c1'] = 100
d2['l1'][0] = 10 #os números ficam salvos na memória de ambas as variáveis

d3 = copy.deepcopy(d1) #com isso, apenas uma variável é afetada
d3['l1'][1] = 100

print(d1)
print(d2)
print(d3)