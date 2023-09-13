from threading import Thread
from threading import Lock
from time import sleep

# Com threads você pode fazer execuções em paralelo
# Úteis para processos demorados que podem prejudicar seu serviço
# assim o usuario não tem que ficar esperando um processo longo para poder
# navegar no sistema

# usando classe para manipular threads
# class MyThread(Thread):
#     def __init__(self, text: str, time: int):
#         self.text = text
#         self.time = time

#         super().__init__()

#     def run(self):
#         sleep(self.time)
#         print(self.text)


# t1 = MyThread('thread 1', 2)
# t1.start()

# t2 = MyThread('thread 2', 4)
# t2.start()

# t3 = MyThread('thread 3', 6)
# t3.start()

# Com os threads assima, eu consigo executar em paralelo com o for

# for i in range(20):
#     print(i)
#     sleep(1)

# posso passar uma função pra ser executada em um thread paralelo:
# def take_time(text, time):
#     sleep(time)
#     print(text)


# t = Thread(target=take_time, args=('Hellow Word', 5))
# t.start()

# for i in range(20):
#     sleep(2)
#     print(i)


# def take_time(text, time):
#     sleep(time)
#     print(text)

# t = Thread(target=take_time, args=('Hellow Word', 5))
# t.start()

# # esperando a thread acabar:
# # while t.is_alive():
# #     print('Esperando a thread...')
# #     sleep(2)
# # mesma coisa que o while para esperar a thread acabar:
# t.join()

# print('thread acabou')

class Ingressos:
    def __init__(self, stock):
        # para não ter problema com processos que demoram e prejudique
        # a sequencia:
        self._lock = Lock()

        self.stock = stock

    def buy(self, qntd):
        self._lock.acquire()
        # o método acima faz com que as threads ficam bloqueadas até eu liberar

        if self.stock < qntd:
            print('Ingressos insuficientes')
            # para liberar as threads que ficaram presas nessa condição:
            self._lock.release()
            return

        # aqui pode ter um processo complexo que demore:
        sleep(1)
        # isso segura as threads na condição anterior e não permite que todas
        # sigam uma sequencia e faça as próximas interações

        self.stock -= qntd
        print('Compra realizada')
        print(f'ainda temos {self.stock} ingressos')
        print()

        # aqui ocorre a liberação para as threads finalizarem a execução
        # do método buy
        self._lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(10):
        t = Thread(target=ingressos.buy, args=(i, ))
        t.start()

    print(ingressos.stock)
