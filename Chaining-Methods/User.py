#User

class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0
    def make_deposit(self, amount):
        self.amount += amount
        return self
    def make_withdrawl(self,amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

guido = User("Guido van Rossum")
margaret = User("Margaret")
roger = User("Roger")

guido.make_deposit(2700).make_deposit(20).make_deposit(150).make_withdrawl(127).display_user_balance()
margaret.make_deposit(1320).make_deposit(800).make_withdrawl(2000).make_withdrawl(10).display_user_balance()
roger.make_deposit(1).make_withdrawl(1500).make_withdrawl(600).make_withdrawl(2700).display_user_balance()
margaret.transfer_money(400, roger)