

class THBank:
    def __init__(self,name,money,pin1):
        self.name = name
        self.balance = money
        self.pin = pin1

    pin = int(input("Ange ett kontnummer med fyra siffror > "))
    data = []

    if pin < 1000 or pin > 9999:
        print("ERROR: Ogiltigt kontonummer")
        pin = int(input("Testa igen...ange ett kontnummer med fyra siffror"))
        data.append(pin)

    def pincheck(self,pin):
        if pin == data:
            return True
        else:
            return False
        
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self,money):
        if self.balance > money:
            self.balance -= money
            return money
        else:
            return "Ogiligt belopp"
    
    def chechbalance(self):
        return self.balance


    