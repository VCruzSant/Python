# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, msg):
        self._msg = msg
    
    # enviar notificação para que ? para notificação de celular ? notificação no e-mail? sms ?
    # por isso usamos polimorfismo com abstração
    @abstractmethod
    def send_notif(self) -> bool:... #essa setinha é sobre type anotations (dica pra nós mesmos)



class NotificationEmail(Notification):
    def send_notif(self) -> bool:
        print('E-mail: enviando....', self._msg)
        return True

class NotificationSms(Notification):
    def send_notif(self) -> bool:
        print('SMS: enviando....', self._msg)
        return True

# ne = NotificationEmail('Quero te enviar um e-mail sla')
# ne.send_notif()
# # para por o Liskov substution principle em pratica:
# # se eu alterar ne = NotificationEmail('Quero te enviar um e-mail sla') -> por outra subclasse, o programa não deve ser quebrado:
# ns = NotificationSms('Quero te enviar um sms sla')
# ns.send_notif()
# # poderia substituir a classe apenas, mas ja serve como exemplo

# o parametro notif, pode ser alterado, ser outro obj, sem quebrar a aplicação
def notify(notif: Notification):
    notif_sended = notif.send_notif()

    if notif_sended:
        print('Notificação enviada')
        return
    
    print('Notificação não foi enviada')

nne = NotificationEmail('enviando isso por e-mail')
nns = NotificationSms('enviando isso por sms')

notify(nne)

