aantalBolletjes = 0
aantalLiters = 0
bolOfLiter = ""

def partOfZak():
    klantType = int(input("Bent u 1) particulier of 2) zakelijk?: "))
    global bolOfLiter
    while True:
        if klantType == 1:
            bolOfLiter = "bolletje"
            return klantType
        elif klantType == 2:
            bolOfLiter = "liter"
            return klantType
        else:
            print("Sorry, dat snap ik niet..")

def bolletjesKiezen():
    while True:
        aantalBolletjes = int(input(f"Hoeveel {bolOfLiter}s wilt u?: "))
        if bolOfLiter == "bolletje":
            if aantalBolletjes >= 1 and aantalBolletjes <= 3:
                return aantalBolletjes
            elif aantalBolletjes >= 4 and aantalBolletjes <= 8:
                return aantalBolletjes
            elif aantalBolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet")
            else:
                print("Sorry, dat snap ik niet..")

        elif bolOfLiter == "liter":
            aantalLiters = aantalBolletjes
            if aantalLiters >= 1:
                return aantalLiters
            else:
                print("Sorry, dat snap ik niet..")

def smakenBolletjes(aantalBolletjes):  
    amount = 1
    while amount <= aantalBolletjes:
        smaakje = input(f"Welke smaak wilt u voor {bolOfLiter} nummer {amount}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ").lower()
        if smaakje == "a" or smaakje == "c" or smaakje == "m" or smaakje == "v":
            amount += 1
        else:
            print("Sorry, dat snap ik niet..")

def bakjeOfHoorn():
    if aantalBolletjes <= 3:
        while True:
            bakofhoorn = input(f"Wilt u deze {aantalBolletjes} bolletje(s) in A) een hoorntje of B) een bakje?: ").lower()
            if bakofhoorn == "a":
                return bakofhoorn
            elif bakofhoorn == "b":
                return bakofhoorn
            else:
                print("Sorry, dat snap ik niet..")
    elif aantalBolletjes >=4 and aantalBolletjes <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantalBolletjes} bolletjes")

def toppings():
    global aantalBolletjes
    while True:
        toppingKeuze = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?: ").lower()
        if toppingKeuze == "a":
            prijsTopping = 0
            return prijsTopping
        elif toppingKeuze == "b":
            prijsTopping = 0.50
            return prijsTopping
        elif toppingKeuze == "c":
            prijsTopping = 0.30 * aantalBolletjes
            return prijsTopping
        elif toppingKeuze == "d" and bakofhoorn == "a":
            prijsTopping = 0.60
            return prijsTopping
        elif toppingKeuze == "d" and bakofhoorn == "b":
            prijsTopping = 0.90
            return prijsTopping
        else:
            print("Sorry, dat snap ik niet..")

def bonnetje():
    print("---------[Papi Gelato]---------")
    print("")
    if klantType == 1:
        if aantalBolletjes >= 1:
            print(f"Bolletjes       {aantalBolletjes} x €1.10   = €{round(aantalBolletjes * 1.10, 2)}")
        if bakofhoorn == "a":
            print("Hoorntje        1 x €1.25   = €1.25")
            totaalPrijs = aantalBolletjes * 1.10 + 1.25 + prijsTopping
        elif bakofhoorn == "b":
            print("Bakje           1 x €0.75   = €0.75")
            totaalPrijs = aantalBolletjes * 1.10 + 0.75 + prijsTopping
        if prijsTopping >= 0.1:
            print(f"Topping         1 x {round(prijsTopping , 2)}     = {round(prijsTopping , 2)}" )
        print("                           -------- +")
        print(f"Totaal                        €{round(totaalPrijs, 2)}")
    elif klantType == 2:
        if aantalLiters >= 1:
            print(f"Liter       {aantalLiters} x 9.80   = €{round(aantalLiters * 9.80, 2)}")
            totaalPrijs = aantalLiters * 9.80
        print(f"Totaal                   €{round(totaalPrijs, 2)}")
        print(f"BTW (9%)                 €{round(totaalPrijs / 100 * 9, 2)}")
#-------------------------------------------------------------------------------------#
print("Welkom bij Papi Gelato.") 
klantType = partOfZak() 
if klantType == 1:
    aantalBolletjes = bolletjesKiezen()
    smakenBolletjes(aantalBolletjes)    
    bakofhoorn = bakjeOfHoorn()
    prijsTopping = toppings()
    bonnetje()
elif klantType == 2:
    aantalLiters = bolletjesKiezen()
    aantalBolletjes = aantalLiters
    smakenBolletjes(aantalBolletjes)
    bonnetje()