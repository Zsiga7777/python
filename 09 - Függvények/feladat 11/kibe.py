def bekeresNev()->str:
    nev:str=None
    temp:str = None
    isnev: bool = False

    while ((nev == None) or isnev== False or len(nev) < 2 ):
        print("Kérem a nevét:", end='')
        temp = input()
        isnev = temp.isalpha()

        if (isnev):
            nev = (temp)
        else:
            print("Nem nevet adott meg.")
    return nev

def bekeresSzam()->int:
    szam:int=None
    temp:str = None
    tempMasolat:str = None
    isSzam: bool = False

    while ((szam == None) or isSzam== False or szam <0):
        print("Kérema a ledolgozott órák számát:", end='')
        temp = input()
        tempMasolat = temp.replace("-", "").replace(".","")
        isSzam = tempMasolat.isnumeric()

        if (isSzam):
            szam = int(temp)
        else:
            print("Nem óra számot adott meg meg.")
    return szam

def kiiras(ora:int, fiz:int, nev:str)->None:
    print(f"{nev}, ön {ora} órát dolgozott, és {fiz} Ft-ot keresett")