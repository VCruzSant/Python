# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random

# funções
# seed -> originalmente usa o micro segundos do tempo
# -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(2)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(0, 10, 2)
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(1, 15)
print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(1, 2)
print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
list_name = ['v', 'i', 'n', 'i']
random.shuffle(list_name)
print(list_name)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
new_name = random.sample(list_name, k=3)
print(new_name)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
new_name_repeat = random.choices(list_name, k=3)
print(new_name_repeat)

# random.choice(Iterável) -> Escolhe um elemento do iterável
a_name = random.choice(list_name)
print(a_name)
