import random
import sys
 
class ATM():
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
         
    def account_detail(self):
        print("\n----------HUVUDMENY----------")
        print(f"Kontoägare: {self.name.upper()}")
        print(f"Kontonummer: {self.account_number}")
        print(f"Nuvarande saldo: Nu.{self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Nuvarande saldo: Nu.", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Ogiltig saldo!")
            print(f"Din nuvarande saldo, Nu.{self.balance} .")
            print("testa med en mindre saldo.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} uttag godkännt!")
            print("Nuvarande saldo: Nu.", self.balance)
            print()
 
    def check_balance(self):
        print("Nuvarande saldo: Nu.", self.balance)
        print()
 
    def transaction(self):
        print("""
            KONTOMENY 
        *********************
            Meny:
            1. Ta ut pengar
            2. Sätt in pengar
            3. Visa saldo
            4. Avsluta
        *********************
        """)
        
        while True:
            try:
                option = int(input("Ange 1, 2, 3 eller 4:"))
            except:
                print("ERROR: Ange 1, 2, 3 eller 4!\n")
                continue
            else:
                if option == 1:
                    amount = int(input("Hur mycket vill du ta ut (Nu.):"))
                    atm.withdraw(amount)
                elif option == 2:
                    amount = int(input("Hur mycket vill du sätta in (Nu.):"))
                    atm.deposit(amount)
                elif option == 3:
                    atm.check_balance()
                elif option == 4:
                    print(f"""
                Printar kvitto..............
          ******************************************
              Transaktioner är nu färdiga.                         
              Transaktion nummer: {random.randint(10000, 1000000)} 
              Kontoägare: {self.name.upper()}                  
              Kontonummer: {self.account_number}                
              Slutlig saldo: Nu.{self.balance}                    
 
              Tack för att du använder oss som bank.                  
          ******************************************
          """)
                    sys.exit()
                 
 
print("   ***TEKNIKHÖGSKOLAN BANK***  ")
print("________________________________\n")
print("----------SKAPA KONTO----------")
name = input("Ange namn: ")
account_number = input("Ange kontonummer: ")
print("Grattis! Du har nu skapat ett konto hos oss......\n")
 
atm = ATM(name, account_number)
 
while True:
    trans = input("Vill du göra några transaktioner?(j/n):")
    if trans == "j":
        atm.transaction()
    elif trans == "n":
        print("""
    ----------------------------------------
   | Tack för att du använder oss som bank |
   | Välkommen åter!                       |
    ----------------------------------------
        """)
        break
    else:
        print("Fel kommando!  Ange 'j' för JA och 'n' för NEJ.\n")
    