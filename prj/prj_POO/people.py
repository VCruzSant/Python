import account


class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attr = f'{self.name!r}, {self.age!r}'
        return f'{class_name}({attr})'


class Customer(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.accounter: account.Account | None = None


if __name__ == '__main__':
    c1 = Customer('Vini', 20)
    print(c1)
    c1.accounter = account.CheckingAccount(111, 11, 0, 0)
    c1.accounter.details()
