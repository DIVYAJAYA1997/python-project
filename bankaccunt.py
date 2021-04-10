class Bank:
    def create_accunt(self,accno,minbalance,name):
        self.name=name
        self.balance=minbalance
        self.accnum=accno

    def deposit(self,amunt):
        self.balance+=amunt
        print("BALANCE AMOUNT IS:",self.balance)

    def withdraw(self,value):
        if value>=self.balance:
            print("UNAVAILABLE TO WITHDRAW")
        else:
            self.balance-=value
            print("AVAILABLE BALANCE IS:",self.balance)
obj=Bank()
obj.create_accunt(6701146,5000,"ASDFG")
obj.withdraw(2000)

