"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
import abc


class Account(abc.ABC):
    def __init__(
            self, agency: int, account_id: int, balance: float = 0
    ) -> None:
        self.agency = agency
        self.account_id = account_id
        self.balance = balance

    @abc.abstractmethod
    def take(self, value: float) -> float: ...

    def deposit(self, value: float) -> float:
        self.balance += value
        self.details(f'Depositing: {value}')
        return self.balance

    def details(self, msg: str = '') -> None:
        print(f'your balace is {self.balance:.2f} -> {msg}')


class SavingsAccount(Account):
    def take(self, value):
        value_after_take = self.balance - value

        if value_after_take >= 0:
            self.balance -= value
            self.details(f'Taking: {value}')
            return self.balance
        print('Não foi possivel sacar seu saldo')
        self.details(f'Saque negado {value}')


class CheckingAccount(Account):
    def __init__(
            self, agency: int, account_id: int, balance: float = 0,
            limit: float = 0
    ) -> None:
        super().__init__(agency, account_id, balance)
        self.limit = limit

    def take(self, value: float):
        value_after_take = self.balance - value
        max_limit = -self.limit

        if value_after_take >= max_limit:
            self.balance -= value
            self.details(f'Taking: {value}')
            return self.balance
        print('Unable to withdraw your balance')
        print(f'Your limit is {self.limit:.2f}')
        self.details(f'take denied {value}')

    def __repr__(self):
        class_name = type(self).__name__
        attr = f'{self.agency!r}, {self.account_id!r}, {self.balance!r}, '\
            f'{self.limit!r}'
        return f'{class_name}({attr})'


if __name__ == '__main__':
    # cp1 = SavingsAccount(111, 11)
    # cp1.take(100)
    # cp1.details()
    # print()
    cc1 = CheckingAccount(111, 11, 0, 100)
    cc1.take(101)
    cc1.details()
