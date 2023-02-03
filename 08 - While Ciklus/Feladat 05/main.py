from os import system

szam:str=None
szamMasolat: str = None
osszeg:float=0
db:int=0
hatarertek:str = None
hatarertekmasolat:str = None
while (hatarertek == None or hatarertek < 100 ):
    print("Kérek egy határértéket: ", end='')
    hatarertek = input()
    hatarertekmasolat = hatarertek.replace(".", "").replace("-","")
    if(hatarertekmasolat.isnumeric()):
        hatarertek = float(hatarertek)
    else:
        hatarertek = None

while (osszeg == None or osszeg<hatarertek):
    print("Kérek egy új számot: ", end='')
    szam = input()
    szamMasolat = szam.replace(".", "").replace("-", "")
    if(szamMasolat.isnumeric()):
        szam = float(szam)
        osszeg = osszeg +szam
    db +=1
    
    print(f"Jelenleg az összeg {osszeg}")

system('cls')

print(f"A határérték {hatarertek} volt. A végső összeg {osszeg} lett és {db} leütés kellett hozzá.")