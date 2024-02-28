class Bank :
    def __init__(self):
        self.accounts = {}
  
    def openAccount(self, account):
        self.accounts[account.acc_number] = account
    def closeAccount(self,acc_number):
        if acc_number in self.accounts:
            del self.accounts[acc_number]
        else:
            print("Account not found")
    def ListAllAccounts(self):
        for acc_number, account in self.accounts.items():
            print(f"Account Number: {acc_number}, Owner: {account.acc_owner}, Balance: {account.balance}")
    
    def SearchForAccount(self, acc_number):
        found = False
        for acc_number, account in self.accounts.items():
            if account.acc_number == acc_number:
                found = True
                print(f"Account Number: {acc_number}, Owner: {account.acc_owner}, Balance: {account.balance}")
        if not found:
            print(f"Account {account.acc_number} does not exist.")
    


class Account:
    def __init__(self, acc_number, acc_owner, balance = 0):
        self.acc_number = acc_number
        self.acc_owner = acc_owner 
        self.balance = balance

    def deposit(amount):
        self.balance += amount

    def withdraw(amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Balance is " + self.balance + " it is not sufficent.")

    def check_balance():
        return self.balance

class SavingsAccount(Account):
    def __init__(self, acc_number, acc_owner, balance=0, interest_rate=0.05):
        super().__init__(acc_number, acc_owner,balance)
        self.interest_rate = interest_rate

    def add_interest():
        self.balance += self.balance * self.interest_rate

class WomenAccount(Account):
    def __init__(self, acc_number, acc_owner, balance=0, interest_rate=0.08):
        super().__init__(acc_number, acc_owner,balance)
        self.interest_rate = interest_rate

    def add_interest():
        self.balance += self.balance * self.interest_rate

class customer:
    def __init__(self, customer_id, name, address, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.contact_info = contact_info


class Transaction:
    def __init__(self, trans_id, acc_number, amount, trans_type):
        self.trans_id = trans_id
        self.acc_number = acc_number
        self.amount = amount
        self.trans_type = trans_type
    

#  using the objects and creating instances 

acc1 = SavingsAccount("SA001", "Samuel", 2000)
acc2 = WomenAccount("WA001", "Abigail", 3000)

NigdBank = Bank()

NigdBank.openAccount(acc1)
NigdBank.openAccount(acc2)

print("List of all accounts: ")
NigdBank.ListAllAccounts()

print("\nSearch for an account with id 'SA001'")
NigdBank.SearchForAccount("SA001")

print("\nSearch for an account with id 'SA002'")
NigdBank.SearchForAccount("SA002")

print("close account")
NigdBank.closeAccount("SA001")

print("List of all accounts: ")
NigdBank.ListAllAccounts()
