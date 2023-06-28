import account
import people


class Bank:
    def __init__(
        self, agencies: list[int] | None = None,
        customer: list[people.People] | None = None,
        account: list[account.Account] | None = None,
    ):
        self.agencies = agencies or []
        self.customer = customer or []
        self.account = account or []

    def _check_agency(self, account):
        if account.agency in self.agencies:
            print('_check_agency', True)
            return True
        print('_check_agency', False)
        return False

    def _check_customer(self, customer):
        if customer in self.customer:
            print('_check_customer', True)
            return True
        print('_check_customer', False)
        return False

    def _check_account(self, account):
        if account in self.account:
            print('_check_account', True)
            return True
        print('_check_account', False)
        return False

    def _check_cust_acc(self, customer, account):
        if account is customer.accounter:
            print('_check_cust_acc', True)
            return True
        print('_check_cust_acc', False)
        return False

    def auth(self, customer: people.People, account: account.Account):
        return self._check_agency(account) and \
            self._check_account(account) and \
            self._check_customer(customer) and \
            self._check_cust_acc(customer, account)

    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = f'({self.agencies}, {self.customer}, {self.account})'
        return f'{class_name!r}{attrs!r}'


if __name__ == '__main__':
    c1 = people.Customer('Vini', 20)
    cc1 = account.CheckingAccount(111, 11, 100000)
    c1.accounter = cc1

    c2 = people.Customer('Ni', 20)
    cs2 = account.SavingsAccount(112, 12, 100000)
    c2.accounter = cs2

    bank = Bank()
    bank.customer.extend([c1, c2])
    bank.account.extend([cc1, cs2])
    bank.agencies.extend([111, 112])

    if bank.auth(c1, cc1):
        cc1.deposit(100)
