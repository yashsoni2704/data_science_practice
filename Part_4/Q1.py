class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def check_balance(self):
        return self.balance
    
t1 = BankAccount(1,"Yash",10000)
t1.deposit(15000)
t1.withdraw(25000)
print(t1.account_number,t1.owner_name,t1.balance)