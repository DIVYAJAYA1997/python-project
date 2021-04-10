class Bank:

    def __init__(self, accno, minbalance, name):
        self.name = name
        self.balance = minbalance
        self.accnum = accno

    def deposit(self, amunt):
        self.balance += amunt
        print("BALANCE AMOUNT IS:", self.balance)

    def withdraw(self, value):
        if value >= self.balance:
            print("UNAVAILABLE TO WITHDRAW")
        else:
            self.balance -= value
            print("AVAILABLE BALANCE IS:", self.balance)
obj=Bank(67011461,10000,"asdfgh")
obj.withdraw(2000)
obj1=Bank(112034,5000,"ZXCVBNM")
obj1.deposit(5000)



