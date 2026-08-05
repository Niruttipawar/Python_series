class Acount:
    def __init__(self, name, balance):
        self.name = name
        self.bal = balance

    def deposit(self, amount):
        self.bal += amount
        print(f"creadited... {amount}.current balance is {self.bal}")


    def withdrawal(self, amount):
        self.bal -= amount
        print(f"debited.. {amount}. current balance is {self.bal}")

    def get_bal(self):
        return self.bal

acc1 = Acount ("Nivrutti", 50000)
acc1.deposit(5000)
acc1.withdrawal(0)    
