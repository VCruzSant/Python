# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

# def recursive(init=0, end=10):
     # caso recursivo: contar até chegar no ultimo valor
#     if init == end: # sem isso causa stack overflow -> sobrecarregando a call stack
#         return print(end)

#     init +=1
#     return recursive(init, end)

# recursive()
#limite de 1000

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))