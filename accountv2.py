class BankAccount:
    def __init__(self, name, balance=0.00):
        self.name = name
        self._balance = balance
        self._flag = 1
        
#pythonic way to use getters and setters    
    @property
    def balance(self):
        """check the balance"""
        if self._flag != 1:
            raise ValueError('Account closed')
        return self._balance        

    def open(self):
        self.balance = 0
        self.flag = 1

    def deposit(self, amount):
        """make a deposit"""
        if self._flag != 1:
            raise ValueError('Account closed')
        if amount < 0:
        	raise ValueError("invalid amount")
        self._balance += amount

    def withdraw(self, amount):
        """make a withdraw"""
        if self._flag != 1:
            raise ValueError('Account closed')
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    def close(self):
        self.flag = 0

    def __repr__(self):
        return '{0.__class__.__name__}(name={0.name}, balance={0.balance})'.format(self)

    def __str__(self):
        return 'Bank account of {}, current balance: {}'.format(self.name, self.balance)
    
customer1 = BankAccount('Vivian')
print(repr(customer1))
customer1.deposit(50000)
customer1.withdraw(3000)
print(customer1)
customer2 = BankAccount('Nabulo', 200000)
print(customer2.balance)