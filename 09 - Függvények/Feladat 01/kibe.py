def bekeres()->float:
    szam:float=None
    temp:str = None
    isSzam: bool = False
    tempMasolat :str = None

    while ((szam == None) or isSzam== False):
        print("Kérek egy számot:", end='')
        temp = input()
        tempMasolat = temp.replace(".", "").replace("-","")
        isSzam = tempMasolat.isnumeric()

        if (isSzam):
            szam = float(temp)
        else:
            print("Nem számot adott meg.")
    return szam

def kiiras(a:float, b:float, eredmeny:float, jel:str)->None:
    print(f"{a} {jel} {b} = {eredmeny}")