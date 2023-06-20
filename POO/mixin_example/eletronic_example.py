from log_example import LogPrintMixin

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._on = False

    def put_on(self):
        if not self._on:
            self._on = True

    def put_off(self):
        if self._on:
            self._on = False

class Smartphone(Eletronic):
    _LOG_PRINT = LogPrintMixin()


    def put_on(self):
        super().put_on()
        msg_formated = f'{self._name} ligou'
        if self._on:
            self._LOG_PRINT.log_succes(msg_formated)


    def put_off(self):
        super().put_off()
        msg_formated = f'{self._name} desligou'
        if not self._on:
            self._LOG_PRINT.log_error(msg_formated)
