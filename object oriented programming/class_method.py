# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection():
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    def set_user(self, user): # -> recebe self
        #setter
        self.user = user

    def set_pass(self, password):
        #setter
        self.password = password

    @classmethod # -> recebe a classe por inteiro
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod # -> somente uma função dentro da classe
    def sum(x, y):
        return x + y


# c1 = Connection()
# print(c1.user)

# c1.set_user('sant')
# print(c1.user)

# c1.set_pass('123456')
# print(c1.password)

c1 = Connection.create_with_auth('santi', 123456)
print(c1.password)