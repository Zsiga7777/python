def bekeres()->str:
    nev:str=None
    temp:str = None
    tempMasolat:str = None
    isnev: bool = False

    while ((nev == None) or isnev== False or len(nev) < 2):
        print("Kérek egy nevet:", end='')
        temp = input()
        tempMasolat = temp.replace(" ", "")
        isnev = tempMasolat.isalpha()

        if (isnev):
            nev = (temp).title().strip()
        else:
            print("Nem nevet adott meg.")
    return nev

def kiiras(a:str)->None:
    print(f"Üdvözlöm {a}!")