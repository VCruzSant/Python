from pathlib import Path

PATH_FILE = Path(__file__).parent /'log_example.txt'

class Log:
    # Assinatura do método
    def _log(self):
        raise NotImplementedError(
            'Implemente o método log...'
        )
    
    def log_succes(self, msg):
        return self._log(f'Succes: {msg}')
    

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    


    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_log = f'{msg} -> {self.__class__.__name__}'
        with open(PATH_FILE, 'a', encoding='utf8') as file:
            file.write(msg_log)
            file.write('\r\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg, '->', self.__class__.__name__)

if __name__ == '__main__':
    lf = LogFileMixin()
    lf.log_succes('Deu bom')
    lf.log_succes('Deu ruim')

    lp = LogPrintMixin()
    lp.log_succes('Deu bom no file')
    lp.log_error('Deu bom no file')