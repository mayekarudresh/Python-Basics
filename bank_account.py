class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def showBalance(self):
        print("Balance:", self.balance)

b = BankAccount()
b.deposit(10000)
b.withdraw(3000)
b.showBalance()