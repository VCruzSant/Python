class Login:
    def __init__(self, host='Localhost'):
        self.user = None
        self.password = None

    def set_login(self, user, password):
        self.user = user
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def make_log(msg):
        return print('log:', msg)

c1 = Login()
c1.set_login('vini', 123123)
print(c1.__dict__)

c2 = Login.create_with_auth('Sant', 890890)
print(c2.__dict__)

c3 = Login.make_log('esse é o log')
