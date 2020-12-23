class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)
        self.intestRate = interestRate

    def interestAmount(self):
        interest_amount = (self.intestRate * self.balance) / 100
        return interest_amount

if __name__ == '__main__':
    suvro_acct = SavingsAccount('Suvro Banerjee', 3000, 0.5)
    print('Account Holder Name : ', suvro_acct.title)
    print('Initial Balance: ', suvro_acct.getBalance())
    suvro_acct.deposit(1000)
    print('Balance after the deposit: ', suvro_acct.getBalance())
    suvro_acct.withdrawal(200)
    print('Balance after withdrawal: ', suvro_acct.getBalance())
    print('The interest amount on the current balance {} is {}'.format(suvro_acct.getBalance(), suvro_acct.interestAmount()))
