# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# def suma(a, b, /): #com essa barra podemos bloquear chamadas de funções nomeadas -> suma(x=1, y=2) 
#     return print(a + b)

# suma(2, 3)
# print(10 * '-')
# suma(x=1, y=2) #vai gerar o erro porque nossa função é Positional-Only Parameters (/)

def sumakey(x, y, *, c): #devo chamar o que está depois do *, passando argumentos nomeados sumakey(1, 1, c=1)
    return print(x + y + c)

sumakey(1, 1, c=1)