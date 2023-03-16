def bekeresSzoveg()->str:
    deviza:str=None
    temp:str = None
    isdeviza: bool = False

    while ((deviza == None) or isdeviza== False or len(deviza) > 3 or (deviza != "USD" and deviza != "JPY" and deviza !="CHF" )):
        print("Kérem a cél devizát (USD = dollár, JPY = japán jen, CHF = svájci frank):", end='')
        temp = input().upper()
        isdeviza = temp.isalpha()

        if (isdeviza):
            deviza = (temp)
        else:
            print("Nem devizát adott meg.")
    return deviza

def bekeresSzam()->float:
    szam:str=None
    temp:str = None
    tempMasolat:str = None
    isSzam: bool = False

    while ((szam == None) or isSzam== False ):
        print("Kérek egy pénz összeget HUF-ban:", end='')
        temp = input()
        tempMasolat = temp.replace("-", "").replace(".","")
        isSzam = tempMasolat.isnumeric()

        if (isSzam):
            szam = float(temp)
        else:
            print("Nem pénz összeget adott meg meg.")
    return szam

def kiiras(ft:float, valtottErtek:float, euro:float, deviza:str)->None:
    print(f"{ft} HUF = {valtottErtek}-{deviza}-al és {euro} eruróval")