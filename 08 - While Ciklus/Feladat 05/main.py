from os import system

szam:str=None
szamMasolat: str = None
szam_e:bool = False
osszeg:float=0
db:int=0
hatarertek:str = None
hatarertekmasolat:str = None
while (hatarertek == None or hatarertek < 100 ):
    print("Kérek egy határértéket: ", end='')
    hatarertek = input()
    hatarertekmasolat = hatarertek.replace(".", "").replace("-","")
    szam_e = hatarertekmasolat.isnumeric()
    if(szam_e == True):
        hatarertek = float(hatarertek)

while (osszeg == None or osszeg<hatarertek):
    print("Kérek egy új számot: ", end='')
    szam = input()
    szamMasolat = szam.replace(".", "").replace("-", "")
    szam_e = szamMasolat.isnumeric()
    if(szam_e == True):
        szam = float(szam)
        osszeg = osszeg +szam
    db +=1
    
    print(f"Jelenleg az összeg {osszeg}")

system('cls')

print(f"A határérték {hatarertek} volt. A végső összeg {osszeg} lett és {db} leütés kellett hozzá.")