def bekeres()->float:
    szam:str=None
    temp:str = None
    tempMasolat:str = None
    isSzam: bool = False

    while ((szam == None) or isSzam== False ):
        print("Kérek egy koordinátát:", end='')
        temp = input()
        tempMasolat = temp.replace("-", "").replace(".","")
        isSzam = tempMasolat.isnumeric()

        if (isSzam):
            szam = float(temp)
        else:
            print("Nem számot adott meg.")
    return szam

def kiiras(a:float)->None:
    print(f"A két pont távolsága:{a} cm")