from os import system

szam:str=None
szamMasolat: str = None
szam_e:bool = False
osszeg:float=0
db:int=0

while (osszeg == None or osszeg<100):
    print("Kérek egy új számot: ", end='')
    szam = input()
    szamMasolat = szam.replace(".", "").replace("-", "")
    szam_e = szamMasolat.isnumeric()
    if(szam_e == True):
        szam = float(szam)
        osszeg = osszeg +szam
    db +=1
    
    print(f"Jelenleg az összeg {osszeg}, és {db} bevitelnél tart.")

system('cls')

print(f"A végső összeg {osszeg} lett és {db} leütés kellett hozzá.")