import abc


class Account(abc.ABC):
    def __init__(self, agency: int, balance: float = 0) -> None:
        self.agency = agency
        self.balance = balance

    @abc.abstractmethod
    def take(self, value: float) -> float | None: ...

    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'Depositing: {value}')
        return self.balance

    def details(self, msg: str = ''):
        print(f'your balance is: {self.balance}R$ {msg}')


class SavingsAccount(Account):
    def take(self, value: float) -> float | None:
        value_after_take = self.balance - value
        if value_after_take >= 0:
            self.balance -= value
            self.details(f'Taking: {value}')
            return self.balance
        print(f'Unable to withdraw your balance {value}')
        self.details()
        return None


class ChekingAccount(Account):
    def __init__(self,
                 agency: int,
                 balance: float = 0,
                 limit: float = 0
                 ) -> None:
        super().__init__(agency, balance)
        self.limit = limit

    def take(self, value: float) -> float | None:
        value_after_take = self.balance - value
        if value_after_take >= -self.limit:
            self.balance -= value
            self.details(f'Taking: {value}')
            return self.balance
        print(f'Unable to withdraw your balance {value}')
        self.details()
        return None


if __name__ == '__main__':
    # sa1 = SavingsAccount(111)
    # sa1.details()
    # sa1.take(1)
    # sa1.deposit(2)
    # sa1.deposit(2)
    # sa1.take(1)
    # sa1.take(4)
    ca1 = ChekingAccount(112)
    ca1.details()
    ca1.take(1)
    ca1.deposit(2)
    ca1.deposit(2)
    ca1.take(1)
    ca1.take(4)
