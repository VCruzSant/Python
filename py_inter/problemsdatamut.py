#problemas dos parametros mutaveis em funções python

def add_customer(name, list_c=None): #toda vez que eu chamar a função sem passar a lista que eu quero, a função vai criar a lista e adicionar o valor passado
    if list_c is None:
        list_c = []
    list_c.append(name)
    return list_c



list_1 = []
cust_1 = add_customer('santiago', list_1)
add_customer('cruz', cust_1)
print(cust_1)

cust_2 = add_customer('vini')
add_customer('dacruz', cust_2)
print(cust_2)
