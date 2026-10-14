class Saving:
    def __init__(self,actno,bal):
        self.actno=actno
        self.bal=bal
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("amount deposited successfully")
    def show_balance(self):
        return f"balance is {self.bal}"
a=int(input("Enter account number"))
b=int(input("Enter balance"))
s=Saving(a,b)
amt=int(input("enter amount to be deposited"))
s.deposit(amt)
print(s.show_balance())
