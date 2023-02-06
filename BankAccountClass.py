"""
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
Give the complete code for the  BankAccount class.
"""

class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "is successful. Available balance:", self.balance)

    def Withdrawal(self,amount):
        if amount > self.balance:
            print("Withdrawal failed. Not enough balance.")
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "is successful. Available balance:", self.balance)

    def bankFees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print("Bank fees of", fee, "applied. Available balance:", self.balance)

    def display(self):
        return f"\nAccount Number: {self.accountNumber}\nName: {self.name}\nBalance: {self.balance}\n"

if __name__ == '__main__':
    acc = BankAccount(123, "John Smith",1000)
    print(acc.display())

    acc.Deposit(500)
    acc.Withdrawal(300)
    acc.bankFees()
