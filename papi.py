aantalBolletjes = 0
totaalBolletjes = 0
aantalLiters = 0
bolOfLiter = ""
totaalHoorn = 0
totaalBakje = 0
totaalTopping = 0

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
            print("Sorry, dat is geen optie die we aanbieden..")

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
                print("Sorry, dat is geen optie die we aanbieden..")

        elif bolOfLiter == "liter":
            aantalLiters = aantalBolletjes
            if aantalLiters >= 1:
                return aantalLiters
            else:
                print("Sorry, dat is geen optie die we aanbieden..")

def smakenBolletjes(aantalBolletjes):  
    amount = 1
    while amount <= aantalBolletjes:
        smaakje = input(f"Welke smaak wilt u voor {bolOfLiter} nummer {amount}? A) Aardbei, C) Chocolade of V) Vanille?: ").lower()
        if smaakje == "a" or smaakje == "c" or smaakje == "v":
            amount += 1
        else:
            print("Sorry, dat is geen optie die we aanbieden..")

def bakjeOfHoorn():
    global totaalHoorn
    global totaalBakje
    if aantalBolletjes <= 3:
        while True:
            bakofhoorn = input(f"Wilt u deze {aantalBolletjes} bolletje(s) in A) een hoorntje of B) een bakje?: ").lower()
            if bakofhoorn == "a":
                bakofhoorn = "hoorntje"
                totaalHoorn += 1
                return bakofhoorn
            elif bakofhoorn == "b":
                bakofhoorn = "bakje"
                totaalBakje += 1
                return bakofhoorn
            else:
                print("Sorry, dat is geen optie die we aanbieden..")
    elif aantalBolletjes >=4 and aantalBolletjes <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantalBolletjes} bolletjes")
        bakofhoorn = "bakje"
        totaalBakje += 1
        return bakofhoorn

def extraBestellen():
    global totaalBolletjes
    global totaalTopping
    totaalBolletjes = totaalBolletjes + aantalBolletjes
    totaalTopping = totaalTopping + prijsTopping

    while True:
        extra = input(f"Hier is uw {bakofhoorn} met {aantalBolletjes} bolletje(s). Wilt u nog meer bestellen? (Y/N): ").lower()
        if extra == "y":
            return extra
        elif extra == "n":
            print("Bedankt en tot ziens!")
            return extra
        else:
            print("Sorry, dat is geen optie die we aanbieden..")

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
        elif toppingKeuze == "d" and bakofhoorn == "hoorntje":
            prijsTopping = 0.60
            return prijsTopping
        elif toppingKeuze == "d" and bakofhoorn == "bakje":
            prijsTopping = 0.90
            return prijsTopping
        else:
            print("Sorry, dat is geen optie die we aanbieden..")

def bonnetje():
    print("---------[Papi Gelato]---------")
    print("")
    if klantType == 1:
        totaalPrijs = totaalBolletjes * 0.95 + totaalHoorn * 1.25 + totaalTopping + totaalBakje * 0.75
        if aantalBolletjes >= 1:
            print(f"Bolletjes       {totaalBolletjes} x €0.95   = €{round(totaalBolletjes * 0.95, 2)}")
        if totaalHoorn >= 1:
            print(f"Hoorntje        {totaalHoorn} x €1.25   = €{totaalHoorn * 1.25}")
        if totaalBakje >= 1:
            print(f"Bakje           {totaalBakje} x €0.75   = €{totaalBakje * 0.75}")
        if totaalTopping >= 0.1:
            print(f"Topping         1 x {round(totaalTopping , 2)}     = {round(totaalTopping , 2)}" )
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
extra = "y" 
if klantType == 1:
    while extra == "y":
        aantalBolletjes = bolletjesKiezen()
        smakenBolletjes(aantalBolletjes)    
        bakofhoorn = bakjeOfHoorn()
        prijsTopping = toppings()
        extra = extraBestellen()
    bonnetje()

elif klantType == 2:
    aantalLiters = bolletjesKiezen()
    aantalBolletjes = aantalLiters
    smakenBolletjes(aantalBolletjes)
    bonnetje()