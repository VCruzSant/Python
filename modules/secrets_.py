# secrets gera números aleatórios seguros
import secrets
import string as s

random = secrets.SystemRandom()
# posso usar todos os métodos da lib random original aqui nesse SystemRandom
# com ele, a aleatoriedade se torna segura
print(''.join(
    random.choices(
        s.ascii_letters + s.digits + s.punctuation, k=10
    )
)
)
