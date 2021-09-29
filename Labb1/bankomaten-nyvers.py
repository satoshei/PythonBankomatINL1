class Bank:
    def __init__(self):
        self.amount = 0
        self.account = ""
    
    kontonummer = True
    kontoLista = []

    def welcome(self):
        self.account = int(input("Ange ett fyra siffrigt kontonummer: "))
        if self.account < 1000 or self.account > 9999:
            print("Ogiltigt kontonummer testa igen >")
        else:
            print("--------------------------")
            print("      ***TH-BANK***   ")
            print("      ***Konto***", self.account)
            print("--------------------------")
            print("1. Skapa konto")
            print("2. Adminstrera konto")
            print("3. Avsluta")

    def balance(self):
        print("Ditt nuvarande saldo: {}".format(self.amount))
    
    def deposit(self):
        self.amount += float(input("Ange ett belopp för insättning : ".format(self.account)))
    
    def withdraw(self):
        withdrawAmount = float(input("Ange ett belopp för uttag: "))

        if withdrawAmount > self.amount:
            print("Ogiligt uttags belopp")
        else:
            self.amount -= withdrawAmount
        
        self.balance()
    
    def createAccount(self):
        print("Du skapar nu ett konto hos oss :)")
        nmr = int(input("Ange ett kontonummer med fyra siffror: "))
        found_account = False
        while nmr < 1000 or nmr > 9999:
            nmr = int(input("Ogiltigt kontonummer..Testa igen: "))
            self.account = nmr
            found_account = True
        if found_account == False:
            print("Felaktigt kontonummer...testa igen")

    def adminAccount(self):
        while True:
            print("*** KONTOMENY *** ")
            print("1. Ta ut")
            print("2. Saldo")
            print("3. Insätt")
            print("4. Tillbaka")

            cmd = int(input("Välj ett alternativ: "))

            if cmd == 2:
                Bank.balance()
            elif cmd == 1:
                Bank.deposit
            elif cmd == 3:
                Bank.withdraw
            else:
                print("Var snäll och ange ett valbart altenativ")