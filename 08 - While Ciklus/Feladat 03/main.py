import random

randszam :int =random.randrange(1,9)
tip:str=None
tipMasolat:str=None
elet:int=6
kitalalta_e:bool = False
szam_e:bool = False

while (tip == None or randszam != tip ):
    elet -= 1
    print(f"még {elet} éltete van \nKérek egy számot:", end='')
    tip =(input())
    tipMasolat = tip.replace(".", "").replace("-","")
    szam_e = tipMasolat.isnumeric()
    if(szam_e == True):
        float(tip)
    if(elet == 1):
        break

if(tip == randszam):
    print(f"Gratulálok! A helyes szám a {randszam} volt.")
else:
    print(f"Sajnos nem találta ki. A helyes szám {randszam} volt")
