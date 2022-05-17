# declaration of class
class Atm() :
    #declaring a constructor
    def __init__(self, pinNumber, cardNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    #declaring a function self=this
    def CashWithdrawal(self):
        print("Cash withdrawn")

    def BalanceEnquiry(self):
        print("Balance")

semwe = Atm("200123","911095")
print(semwe.BalanceEnquiry)
print(semwe.CashWithdrawal())