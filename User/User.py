#User

class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0
    def make_deposit(self, amount):
        self.amount += amount
    def make_withdrawl(self,amount):
        self.amount -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

guido = User("Guido van Rossum")
margaret = User("Margaret")
roger = User("Roger")

guido.make_deposit(2700)
guido.make_deposit(20)
guido.make_deposit(150)
guido.make_withdrawl(127)
guido.display_user_balance()

margaret.make_deposit(1320)
margaret.make_deposit(800)
margaret.make_withdrawl(2000)
margaret.make_withdrawl(10)
margaret.display_user_balance()

roger.make_deposit(1)
roger.make_withdrawl(1500)
roger.make_withdrawl(600)
roger.make_withdrawl(2700)
roger.display_user_balance()

margaret.transfer_money(400, roger)