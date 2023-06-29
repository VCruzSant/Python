import account
import people


class Bank:
    def __init__(self, agencies: list[int] | None = None,
                 customers: list[people.Customer] | None = None,
                 accounts: list[account.Account] | None = None
                 ) -> None:
        self.agencies = agencies or []
        self.customers = customers or []
        self.accounts = accounts or []

    def _check_agencies(self, account: account.Account):
        if account.agency in self.agencies:
            print('_check_agencies', True)
            return True
        print('_check_agencies', False)
        return False

    def _check_customer(self, customer: people.Customer):
        if customer in self.customers:
            print('_check_customer', True)
            return True
        print('_check_customer', False)
        return False

    def _check_account(self, account: account.Account):
        if account in self.accounts:
            print('_check_account', True)
            return True
        print('_check_account', False)
        return False

    def _check_acc_cust(self, customer: people.Customer,
                        account: account.Account
                        ):
        if account is customer.account:
            print('_check_acc_cust', True)
            return True
        print('_check_acc_cust', False)
        return False

    def auth(self, customer: people.Customer, account: account.Account):
        return self._check_agencies(account) and \
            self._check_customer(customer) and \
            self._check_account(account) and \
            self._check_acc_cust(customer, account)


if __name__ == '__main__':
    c1 = people.Customer('Vini', 20)
    sac1 = account.SavingsAccount(111)
    c1.account = sac1

    c2 = people.Customer('Ni', 20)
    sac2 = account.ChekingAccount(112)
    c2.account = sac2

    bank = Bank()
    bank.customers.extend([c1, c2])
    bank.accounts.extend([sac1, sac2])
    bank.agencies.extend([111, 112])

    if bank.auth(c1, sac1):
        print('executei auth')
        c1.account.details('alou')
        c1.account.take(1)
