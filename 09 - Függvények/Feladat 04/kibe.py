from colored import *
def bekeres()->str:
    nev:str=None
    temp:str = None
    tempMasolat:str = None
    isnev: bool = False

    while ((nev == None) or isnev== False or len(nev) < 2):
        print("Kérek egy nevet:", end='')
        temp = input().strip()
        tempMasolat = temp.replace(" ", "")
        isnev = tempMasolat.isalpha()

        if (isnev):
            nev = (temp).title()
        else:
            print("Nem nevet adott meg.")
    return nev

def kiiras(nev:str)->None:
    szam:int=len(nev)
    print (f'%s Üdvözlöm {nev} %s' % (fg(szam), attr(0)))