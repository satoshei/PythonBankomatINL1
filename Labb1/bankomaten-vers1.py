import sys, time, random


user = {
    "balance": 0,
    "account": 0
}

found_account = False

print("--------------------------")
print("***TEKNIKHÖGSKOLAN-BANK***")
print("--------------------------")

print("1. Skapa konto")
print("2. Adminstrera konto")
print("3. Avsluta")

while True:

    sel = input("Ange menyval > ")

    if sel == "1":
        print("Du skapar nu ett konto hos oss :)")
        nmr = int(input("Ange ett kontonummer med fyra siffror: "))
        found_account = False
        while nmr < 1000 or nmr > 9999:
            nmr = int(input("Ogiltigt kontonummer..Testa igen: "))
        user["account"] = nmr
        found_account = True
        if found_account == False:
            print("Felaktigt kontonummer...testa igen")

        print("Ditt kontonummer kommer snart att visas på skärmen, \nvar snäll och skydda dina uppgifter")
        time.sleep(2)
        print("Kontonummer: ",user["account"])
    
    elif sel == "2":
        nmr = int(input("Ange ett kontonummer med fyra siffror: "))
        found_account = False
        if nmr < 1000 or nmr > 9999:
            nmr = int(input("Ogiltigt kontonummer..Testa igen: "))
            user["account"] = nmr
            found_account = True
            if found_account == False:
                print("Felaktigt kontonnummer...testa igen genom att trycka på 'enter' ")


            
        else:
            print("---------------")
            print("***KONTOMENY*** - konto: ", nmr)
            print("---------------")
            print("1. Ta ut pengar")
            print("2. Sätt in pengar")
            print("3. Visa saldo")
            print("4. Avsluta")
            print("---------------")
            
            while True:

                sel = input("Ange menyval > ")

                if sel == "1":
                    belopp = int(input("Ange belopp för uttag: "))
                    if belopp > user["balance"]:
                        print("ERROR: För stort belopp för uttag ")
                        input("Testa igenom genom att trycka 'enter' ")
                    elif belopp <= user["balance"]:
                        user["balance"] = user["balance"] - belopp
                        print("Uttag godkänt du har nu",user["balance"], "kr kvar på ditt konto:",nmr)
                
                elif sel == "2":
                    insätt = int(input("Ange belopp för insättning: "))
                    user["balance"] = user["balance"] + insätt
                    print("Arbetar...")
                    time.sleep(2)
                    print("Du har nu valt att göra en insättning på",insätt,"kr", "på kontonummer",nmr)
                    print("Du har nu",user["balance"], "på ditt konto")
                
                elif sel == "3":
                    print("Ditt saldo visas snart på skärmen, var snäll och skydda dina uppgifter")
                    time.sleep(2)
                    print(user["balance"], ":-")

                elif sel == "4":
                    print("Transaktion är nu klart")
                    print("Transaktionsnummer: ", random.randint(10000, 1000000))
                    print("Tack för att du väljer oss som bank!")
                    exit()