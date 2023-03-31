from os import system

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

def nevekBekeres(munkasSzama:int)->str:
    nevek:str =""
    for i in range(0, munkasSzama, 1):
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

def szamokBekeres(munkasSzama:int)->str:
    szamok:str =""
    for i in range(0, munkasSzama, 1):
        szamok += str( bekeresSzam()) + ","
    return szamok

def kiiras(nevek:str, orak:str, fizetesek:str, munkasSzam:int)->None:
    nev:str=""
    ora:str=""
    fizetes:str=""
    for i in range (0, munkasSzam, 1):
        nev = nevek.split(",")[i]
        ora = orak.split(",")[i]
        fizetes = fizetesek.split(",")[i]
        print(f"{nev}, ön {ora} órát dolgozott, és {fizetes} Ft-ot keresett")
        nev = ""
        ora = ""
        fizetes = ""

def bekeresMunkasSzam()->int:
    szam:int=None
    temp:str = None
    tempMasolat:str = None
    isSzam: bool = False

    while ((szam == None) or isSzam== False or szam <1):
        print("Kérem a munkások számát:", end='')
        temp = input()
        tempMasolat = temp.replace("-", "").replace(".","")
        isSzam = tempMasolat.isnumeric()

        if (isSzam):
            szam = int(temp)
        else:
            print("Nem munkás számot adott meg.")
    return szam