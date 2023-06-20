# Abstração 
from pathlib import Path

# pegando caminho do LogFile
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    # assinatura do método
    def _log(self, msg):
        # Quando esse erro é exibido, vc está usando a super-classe, quando vc deveria usar a sub-class
        raise NotImplementedError(
            'implemente o método Log'
        )
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    

# Mixin -> adicionar coisas nas classes
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formated = (f'{msg} -> {self.__class__.__name__}')
        print('salvando no log', msg_formated)
        # criando um arquivo
        with open(LOG_FILE, 'a', encoding='utf8') as file:
            file.write(msg_formated)
            file.write('\r\n')
  
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} -> {self.__class__.__name__}')
    
    
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('deu ruim')
    lp.log_success('boa')
    lf = LogFileMixin()
    lf.log_error('deu ruim')
    lf.log_success('boa')
    print(LOG_FILE)