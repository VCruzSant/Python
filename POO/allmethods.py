class Connect:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        #setter
        self.user = user

    def set_password(self, password):
        #setter
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        return msg

# c1 = Connect()
# c1.set_user('Vini')
# c1.set_password('123456')

# print(c1.user)
# print(c1.password)

c2 = Connect.create_with_auth('vini', '12345')
print(c2.__dict__)
print(Connect.log('esse é o log'))