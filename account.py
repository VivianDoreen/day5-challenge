"""
a bank account supporting opening/closing,
withdrawals, and deposits of money. 
"""
class BankAccount(object):
    "Implementing methods that enable operation of the bank"
    def __init__(self, name):
        self.flag = 1
        self.name = name

    #checking the available balance
    def get_balance(self):
        if self.flag != 1:#check if the account is open
            raise ValueError('account closed')
        return self.balance

    #open a bank account with initian balance of 0
    def open(self, balance = 0):
        #check if the account is open
        if self.flag != 1:
            raise ValueError('account closed')
        self.balance = balance
        return self.balance 

    def deposit(self, amount):
        #check if the account is open
        if self.flag != 1: 
            raise ValueError('your account is closed')
        if amount <=0:
            raise ValueError('enter a valid amount')

        #get total balance
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        #check if the account is open
        if self.flag != 1: 
            raise ValueError('your account is closed')
        if self.balance < amount:
            raise ValueError("withdraw an amount less than your current balance")
        if amount < 0:
            raise ValueError('Please enter a valid amount')

        #Get remaining balance
        self.balance -= amount
        return self.balance

    def close(self):
        #close account 
        self.flag = 0
        return self.flag
