from typing import *
import os

class Diak:
    def __init__(self) -> None:
        super().__init__()
        self.nev:str=None
        self.osztaly:str=None
        self.jegy:int=0
    def __str__(self) -> str:
        return f"Diák neve:{self.nev}, osztálya:{self.osztaly}, jegye:{self.jegy}"
    
def beolvasas()->List[Diak]:
    fajlnev:str="jegyek.txt"
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    teljesut:str=os.path.join(alaput, fajlnev)
    egysor:str=None
    adat:List=[]
    diak:Diak
    diakok:List[Diak]=[]

    try:
        with open(teljesut, mode="r", encoding="utf-8") as file:
            for sor in file:
                diak=Diak()
                egysor=sor.strip()
                adat=egysor.split(" ")
                diak.nev=adat[0] +" "+ adat[1]
                diak.osztaly=adat[2]
                diak.jegy=int(adat[3])
                diakok.append(diak)
        return diakok
    except FileNotFoundError as er:
        print(f" A fájlal baj van {er.filename}")
        return []
    
def eredmenytelenVizsgazokSzama(diakok:List[Diak])->int:
    eredmeny:int=0
    for diak in diakok:
        if(diak.jegy == 1):
            eredmeny +=1
    return eredmeny

def jelesTanulok(diakok:List[Diak])->List[str]:
    eredmeny:List[str]=[]
    for diak in diakok:
        if(diak.jegy == 5):
            eredmeny.append(diak.nev)
    return eredmeny

def osztalyAtlagSzamitas(diakok:List[Diak])->float:
    osszeg:int=0
    darab:int=0
    for diak in diakok:
        if(diak.osztaly == "10.a"):
            osszeg += diak.jegy
            darab +=1
    return osszeg/darab

diakok:List[Diak] = beolvasas()

print("a) feladat")
diakokSzama=len(diakok)
print(f"{diakokSzama} diák írt dolgozatot.")

print("\nb) feladat")
sikertelenVizsaSzam:int=eredmenytelenVizsgazokSzama(diakok)
print(f"{sikertelenVizsaSzam} diáknak nem sikerült az alapvizsgája.")

print("\nc) feladat \nJeles eredményt elért tanulók:")
jelesek:List[str]=jelesTanulok(diakok)
for i in range(0, len(jelesek), 1):
    print(f"{jelesek[i]}")


print("\nd) feladat")
osztalyatlag:float=osztalyAtlagSzamitas(diakok)
print(f"10.a osztály átlageredménye: {osztalyatlag:1.2f}")