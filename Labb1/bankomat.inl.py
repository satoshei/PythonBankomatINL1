from random import choice   # för att skapa ett random kortnummer
import sqlite3              # för att lagra kund information
import time
import sys

# skapa databas object
conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS customers
(cardNumber INT PRIMARY KEY, name TEXT, surname TEXT, pin INT, mail TEXT, money REAL)''')
conn.commit()

print("\n", "-"*20, "Välkommen till TH-Bank", "-"*20, "\n\n")

# Med den här funktionen konvertera en tuple till en sträng
def tupleToStr(tup): 
    string =  ''.join(tup) 
    return string

# Inte så svårt att förstå vad detta gör :)
def exitProgram():
    print("Loggar ut...")
    time.sleep(1)
    sys.exit(0)

def mainMenu(cardNumber):
    cardNum = cardNumber
    print('''
    #############################################################
    #                                                           #
    # *  Select the bank transaction you want to make. (1-6)    #
    #                                                           #
    # 1. Kontoöversikt                                          #
    # 2. Ändra PIN kod                                          #
    # 3. Uttag                                                  #                
    # 4. Insättning                                             #
    # 5. Överför medel mellan länkade bankkonton                #
    # 6. Avsluta                                                #
    #                                                           #
    #############################################################
    ''')
    
    select = int(input("Menyval: "))

    if select <= 6:
        if select == 1:
            viewAccount(cardNum)
        elif select == 2:
            changePin(cardNum)
        elif select == 3:
            withdraw(cardNum)
        elif select == 4:
            deposit(cardNum)
        elif select == 5:
            transfer(cardNum)
        elif select == 6:
            exitProgram()
    else:
        print("Ange ett heltal (1-6)")
        mainMenu(cardNumber)

def amountOfMoney(cardNumber):
    amountOfMoney = cursor.execute("SELECT money FROM customers WHERE cardNumber=?", (cardNumber,))
    myIter = next(iter(amountOfMoney))
    money = float('.'.join(str(myIt) for myIt in myIter))
    print("\nAmount of current balance:", money)

# Denna funktion visar kundinformation
def viewAccount(cardNumber):
    infoCustomer = tuple(cursor.execute("SELECT * FROM customers WHERE cardNumber=?", (cardNumber,)))
    print("\nKontoöversikt                   ")
    print("----------------------------------")
    print("\nKortnummer:", infoCustomer[0][0])
    print("Namn:", infoCustomer[0][1])
    print("Efternamn:", infoCustomer[0][2])
    print("PIN:", infoCustomer[0][3])
    print("Mail:", infoCustomer[0][4])
    print("Pengar:", infoCustomer[0][5])
    print("----------------------------------\n")
    mainMenu(cardNumber)

# Med den här funktionen kan du skicka pengar till ett annat bankkonto.
def transfer(cardNumber):
    amountOfMoney(cardNumber)
    transferCardNumber = input("\nAnge kortnumret på kontot du ska skicka pengar till: ")
    if transferCardNumber.isdigit() == True:
        transferCardNumber = int(transferCardNumber)
        cursor.execute("SELECT * FROM customers WHERE cardNumber=?", (transferCardNumber,))
        if cursor.fetchone() is not None:
            question = input("\nÄr du säker på att du har angett rätt kortnummer? (ja: y / nej: n): ").lower()
            if question == "y":
                transferMoney = input("\nAnge en summa pengar att skicka: ")
                if transferMoney.isdigit() or transferMoney.isdecimal() == True:                 
                    cursor.execute("UPDATE customers SET money = money + (?) WHERE cardNumber = ?", (transferMoney, transferCardNumber))
                    cursor.execute("UPDATE customers SET money = money - (?) WHERE cardNumber = ?", (transferMoney, cardNumber))
                    conn.commit()
                    print("\nTransaktionen lyckades!\n")
                    mainMenu(cardNumber)
                else:
                    print("Ange INTEGER- eller DECIMAL -nummer")
                    transfer(cardNumber)
            elif question == "n":
                transfer(cardNumber)
            else:
                print("Ogiltigt svar. Försök igen.")
                transfer(cardNumber)
        else:
            print("Ogiltigt kortnummer, försök igen.")
            transfer(cardNumber)
    else:
        print("FEL kortnummer. Ange INTEGER -kortnumret!")
        transfer(cardNumber)

# Med den här funktionen kan du ändra din PIN -kod
def changePin(cardNumber):
    try:
        newPin = int(input("Ange din nya PIN -kod: "))
        cursor.execute("UPDATE customers SET pin = ? WHERE cardNumber=?", (newPin, cardNumber))
        print("\n#############################")
        print("Din nya pin:", newPin)
        print("#############################\n")
        conn.commit()
    except:
        print("\nAnge heltals -PIN\n")
        changePin(cardNumber)
    else:
        mainMenu(cardNumber)

# Med den här funktionen kan du sätta in dina pengar
def deposit(cardNumber):
    amountOfMoney(cardNumber)
    try:
        addMoney = float(input("\nHur mycket pengar vill du sätta in på ditt konto ?: "))
        print("\npengarna sätts in på ditt konto ...\n")
        time.sleep(2)
        
        cursor.execute("UPDATE customers SET money = money + (?) WHERE cardNumber=?", (addMoney, cardNumber))
        conn.commit()
        amountOfMoney(cardNumber)
    except:
        print("\nOgiltigt värde. Var god försök igen.")
        deposit(cardNumber)
    else:
        mainMenu(cardNumber)

# Med den här funktionen kan du ta ut från ditt konto
def withdraw(cardNumber):
    amountOfMoney(cardNumber)
    try:
        addMoney = float(input("\nHur mycket pengar vill du ta ut från ditt konto?: "))
        print("\nPengarna dras ...\n")
        time.sleep(2)

        cursor.execute("UPDATE customers SET money = money - (?) WHERE cardNumber=?", (addMoney, cardNumber))
        amountOfMoney(cardNumber)
        conn.commit()
    except:
        print("\nOgiltigt värde. Var god försök igen.")
        deposit(cardNumber)
    else:
        mainMenu(cardNumber)

# Denna funktion skapar ett konto för kunden
def signUp():
    try:
        cardNumber = choice(range(1000, 10000))
        name = input("Ange ditt namn: ").capitalize()
        surname = input("Ange ditt efternamn: ").capitalize()
        pin = int(input("Ange din PIN kod: "))
        while True:
            mail = input("Ange ett mail (gmail): ")
            if "@gmail.com" in mail:
                break
            else:
                print("\nDu bör använda ett Gmail -konto ('@gmail.com').\n")
        money = float(input("Ange mängden pengar: "))
        cursor.execute(''' INSERT INTO customers VALUES 
        (?, ?, ?, ?, ?, ?)''', (cardNumber, name, surname, pin, mail, money))
        conn.commit()
        infoCustomer = tuple(cursor.execute("SELECT * FROM customers WHERE cardNumber=?", (cardNumber,)))
        print("\nRegistrering lyckad!\n")
        viewAccount(infoCustomer[0][0])
    except:
        print("Ogiltigt värde. Var god försök igen.")
        signUp()
    else:
        mainMenu(cardNumber)

# Med den här funktionen kan du logga in på ditt konto.
def signIn():
    cardNumber = int(input("Ange ditt kortnummer: "))
    pin = int(input("Ange din PIN -kod: "))
    cursor.execute("SELECT * FROM customers WHERE cardNumber=? AND pin=?", (cardNumber, pin))
    if cursor.fetchone() is not None:
        welcomeName = cursor.execute("SELECT name FROM customers WHERE cardNumber=?",(cardNumber,))
        myIter = iter(welcomeName)
        print("\nVälkommen kära kund!,", tupleToStr(next(myIter)))
        mainMenu(cardNumber)
    else:
        print("\nFEL kortnummer eller PIN -kod, försök igen.\n")
        signIn()

while True:
    print('''
    ###################################################
    #                                                 #
    #  Logga in (enter 'i')   Skapa konto (enter 'u') # 
    #                                                 #
    #                 Avsluta (enter 'e')             #
    #                                                 #
    ###################################################
    '''.lower())
        
    question = input("Menyval: ").lower()
    if question == "i":
        signIn()
        break
    elif question == "u":
        signUp()
        break
    elif question == 'e':
        exitProgram()
    else:
        print("Ogiltigt sökord. Försök igen.")