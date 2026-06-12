class BankAccount:
    def _init_(self, account_no,balance):
        self.account_no = account_no
        self.balance = balance
    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)

account1 = BankAccount("964848", 6757000)
account2 = BankAccount("8764757", 806747400)
account3 = BankAccount("0146371s", 5074709)

account1.display()
account2.display()
account3.display()