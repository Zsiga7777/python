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

def nevekBekeres()->str:
    nevek:str =""
    for i in range(0, 5, 1):
        nevek += bekeresNev() + ","
    return nevek
    
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

def szamokBekeres()->str:
    szamok:str =""
    for i in range(0, 5, 1):
        szamok += str( bekeresSzam()) + ","
    return szamok

def kiiras(nevek:str, orak:str, fizetesek:str )->None:
    nev:str=""
    ora:str=""
    fizetes:str=""
    for i in range (0, 5, 1):
        nev = nevek.split(",")[i]
        ora = orak.split(",")[i]
        fizetes = fizetesek.split(",")[i]
        print(f"{nev}, ön {ora} órát dolgozott, és {fizetes} Ft-ot keresett")
        nev = ""
        ora = ""
        fizetes = ""