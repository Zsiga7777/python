def nevbekeres()->str:
    nev:str=None
    temp:str = None
    isnev: bool = False

    while ((nev == None) or isnev== False or len(nev) < 2):
        print("Kérek egy nevet:", end='')
        temp = input()
        isnev = temp.isalpha()

        if (isnev):
            nev = (temp)
        else:
            print("Nem nevet adott meg.")
    return nev

def szuletesBekeres()->int:
    ev:int=None
    temp:str = None
    tempMasolat:str = None
    isev: bool = False

    while ((ev == None) or isev== False or ev< 1000):
        print("Kérek egy születési évet:", end='')
        temp = input()
        tempMasolat = temp.replace("-","" ).replace(".","")
        isev = tempMasolat.isnumeric()

        if (isev):
            ev = int(temp)
        else:
            print("Nem évet adott meg.")
    return ev

def kiiras(nev:str, kor:int)->None:
    print(f"{nev} ön az idén {kor} éves.")