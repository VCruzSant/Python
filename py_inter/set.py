# Sets - Conjuntos em Python (tipo set)
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# s1 = set()  # vazio
# s1 = {'vini', 1, 2, 3}  # com dados
# print(type(s1))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = {'vini', 1, 2, 3, 3, 3, 1} #remove valores duplicados

print(s1) 
print(2 in s1) #tem 2 no set?
for numb in s1:
    print(numb)

# Métodos úteis:
# add, update, clear, discard

s2 = set()

s2.add('algo')
s2.update(('hellow', 1, 2, 3)) #manda iterado no set, para passar strig, coloca entre parenteses, aceita + de 1 valor
s2.discard('hellow')
print(s2)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s10 = {1, 2, 3}
s20 = {2, 3, 4}
su = s10 | s20 
su = s10 & s20 
su = s10 - s20 
su = s10 ^ s20 
print(su)