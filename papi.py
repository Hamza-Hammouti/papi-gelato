aantalBolletjes = 0

def bolletjesKiezen():
    while True:
        aantalBolletjes = int(input("Hoeveel bolletjes wilt u?: "))
        if aantalBolletjes >= 1 and aantalBolletjes <= 3:
            return aantalBolletjes
        elif aantalBolletjes >= 4 and aantalBolletjes <= 8:
            return aantalBolletjes
        elif aantalBolletjes > 8:
            print("Sorry, zulke grote bakken hebben we niet")
        else:
            print("Sorry, dat snap ik niet..")

def smakenBolletjes(aantalBolletjes):
    amount = 1
    while amount <= aantalBolletjes:
        smaakje = input(f"Welke smaak wilt u voor bolletje nummer {amount}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ").lower()
        if smaakje == "a" or smaakje == "c" or smaakje == "m" or smaakje == "v":
            amount += 1
        else:
            print("Sorry, dat snap ik niet..")

def bakjeOfHoorn():
    if aantalBolletjes <= 3:
        while True:
            bakofhoorn = input(f"Wilt u deze {aantalBolletjes} bolletje(s) in A) een hoorntje of B) een bakje?: ").lower()
            if bakofhoorn == "a":
                print("a")
                return bakofhoorn
            elif bakofhoorn == "b":
                print("b")
                return bakofhoorn
            else:
                print("Sorry, dat snap ik niet..")
    elif aantalBolletjes >=4 and aantalBolletjes <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantalBolletjes} bolletjes")

def bonnetje():
    print("---------[Papi Gelato]---------")
    print("")
    print(f"Bolletjes       {aantalBolletjes} x €1.10   = €{round(aantalBolletjes * 1.10, 2)}")
    if bakofhoorn == "a":
        print("Hoorntje        1 x €1.25   = €1.25")
        totaalPrijs = aantalBolletjes * 1.10 + 1.25
    elif bakofhoorn == "b":
        print("Bakje           1 x €0.75   = €0.75")
        totaalPrijs = aantalBolletjes * 1.10 + 0.75
    print("                           -------- +")
    print(f"Totaal                        €{round(totaalPrijs, 2)}")
#-------------------------------------------------------------------------------------#

print("Welkom bij Papi Gelato.")

aantalBolletjes = bolletjesKiezen()

smakenBolletjes(aantalBolletjes)

bakofhoorn = bakjeOfHoorn()

bonnetje()
