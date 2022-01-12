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


    

#-------------------------------------------------------------------------------------#

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
aantalBolletjes = bolletjesKiezen()

bakjeOfHoorn() 