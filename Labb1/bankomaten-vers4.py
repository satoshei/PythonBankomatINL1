class Konto:
    def __init__(self):
        self.Kontonummer = ""
        self.Saldo = 0

kontoLista = []


while True:
    print("***Teknik")
    print("1. Skapa konto")
    print("2. Administrera konto")
    print("3. Exit")
    sel = input("Menyval > ")
    if sel == "3":
        break
    if sel == "1":
        kontonr = input("Ange kontonummer:")
        nyaKontot = Konto()
        nyaKontot.Kontonummer = kontonr
        kontoLista.append(nyaKontot)
    if sel == "2":
        for konto in kontoLista:
            print(f"{konto.Kontonummer} - {konto.Saldo}")

    if sel == "4":
        kontonr = input("Ange kontonummer på konto som du vill ändra:")
        foundAccount = False
        for konto in kontoLista:
            if konto.Kontonummer == kontonr:
                nyttSaldo = float(input("Nytt saldo"))
                konto.Saldo = nyttSaldo
                foundAccount = True
                break
        if foundAccount == False:                
            print("Finns inte...")