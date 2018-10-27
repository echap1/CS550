import random

class BankAccount:
    balance: int
    max_balance: int
    account_name: str
    account_num: int
    account_type: str
    pin: int

    __logged_in = True

    def __init__(self, account_name, account_type, account_num, max_balance=1000000):
        self.balance = 0
        self.account_name = account_name
        self.account_type = account_type
        self.account_num = account_num
        self.pin = random.randint(10000, 100000)
        self.max_balance = max_balance

    def login(self, pin):
        self.__logged_in = pin == self.pin

        return self.__logged_in

    def logout(self):
        self.__logged_in = False

    def get_balance(self):
        if not(self.__logged_in): return False

        return self.balance

    def deposit(self, amount):
        if not (self.__logged_in): return False

        temp = self.balance + amount

        if 0 <= temp <= self.max_balance:
            self.balance = temp

            return True

        return False

    def withdraw(self, amount):
        if not (self.__logged_in): return False

        return self.deposit(-amount)

    def transfer(self, other, amount):
        if not (self.__logged_in): return False

        if other.deposit(amount):
            self.withdraw(amount)

            return True

        return False

    def get_pin(self):
        if not (self.__logged_in): return False

        return self.pin

    def __str__(self):
        if not (self.__logged_in): return "Not Logged In."

        return f"Account: {self.account_name} ({self.account_num}, {self.account_type}) {self.balance}$"
