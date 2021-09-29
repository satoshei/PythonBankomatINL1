import time, random

user = {
    "balance": 0,
    "account": 0
}

def HuvudMeny():
    while True:

        print("--------------------------")
        print("      ***TH-BANK***")
        print("--------------------------")
        print("1. Skapa konto")
        print("2. Adminstrera konto")
        print("3. Avsluta")
        sel = GetSelection(1,3)
        if sel == "3":
            break
        if sel == "2":
            KontoMeny()
        if sel == "1":
            Konto()

def KontoMeny():
    print("*** KONTOMENY *** ")
    print("1. Ta ut")
    print("2. Saldo")
    print("3. Insätt")
    print("4. Tillbaka")
    sel = GetSelection(1,4)
    if sel == "4":
        return
    elif sel == "3":
        Deposit()
    elif sel == "2":
        Saldo()
    elif sel == "1":
        Withdraw()

def Konto(account):
    account = int(input("Ange ett kontonummer med fyra siffror: "))
    if account < 1000 or account > 9999:
        account = int(input("Ogiltigt kontonummer..Testa igen: "))
    else:
        user["account"] = account
        print("Ditt kontonummer kommer snart att visas på skärmen, \nvar snäll och skydda dina uppgifter")
        time.sleep(2)
        print("Kontonummer: ",user["account"])


def GetSelection(min,max):
    while True:
        sel = int(input("Ange val: "))
        if sel >= min and sel <= max:
            return sel

def Deposit(balance):
    balance = user["balance"]
    cmd = int(input("Insättning: Ange hur mycket du vill sätta in på ditt konto > "))
    new_balance = balance + cmd
    print(f"Du har gjort en insättning på {cmd} :- och har nu {new_balance} :- (SEK) på ditt konto")

def Saldo(balance):
    balance = user["balance"]
    print(balance)

def Withdraw(balance):
    balance = user["balance"]
    cmd = int(input("Insättning: Ange hur mycket du vill sätta in på ditt konto > "))
    new_balance = balance - cmd
    print(f"Du har gjort ett uttag på {cmd} :- och har nu {new_balance} :- (SEK) på ditt konto")

HuvudMeny()
KontoMeny()