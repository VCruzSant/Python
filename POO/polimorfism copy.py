from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, msg) -> None:
        self._msg = msg

    @abstractmethod
    def send_notify(self) -> bool: ...

class NotificationEmail(Notification):
    def send_notify(self) -> bool: 
        print(f'E-mail: enviando -> {self._msg}')
        return True
    
class NotificationSms(Notification):
    def send_notify(self) -> bool: 
        print(f'SMS: enviando -> {self._msg}')
        return True

def notify(notif: Notification):
    notif_sended = notif.send_notify()

    if notif_sended:
        print('Notificação enviada')
        return
    print('falha ao enviar notificação')

nne = NotificationEmail('enviando e-mail pra vc')
nns = NotificationSms('enviando e-mail pra vc')

notify(nne)