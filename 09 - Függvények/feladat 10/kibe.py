def bekeresSzam()->int:
    szam:int=None
    temp:str = None
    tempMasolat:str = None
    isSzam: bool = False

    while ((szam == None) or isSzam== False or szam < 0 or szam > 50 ):
        print("Kérek egy számot 0 és 50:", end='')
        temp = input()
        tempMasolat = temp.replace("-", "").replace(".","")
        isSzam = tempMasolat.isnumeric()

        if (isSzam):
            szam = int(temp)
        else:
            print("Nem számot adott meg.")
    return szam

def kiiras(helyesSzam:int, tippSzam:int)->None:
    print(f"Gratulálok, kitalálta a helyes számot, ami {helyesSzam} volt. {tippSzam} db próbából sikerült kitalálni.")