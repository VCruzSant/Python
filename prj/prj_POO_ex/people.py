import account


class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> str:
        self._name = value
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> int:
        self._age = value
        return self._age

    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'


class Customer(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: account.Account | None = None


if __name__ == '__main__':
    c1 = Customer('vini', 20)
    print(c1)
    c1.account = account.ChekingAccount(112)
