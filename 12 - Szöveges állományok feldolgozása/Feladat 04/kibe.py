from varos import *
from typing import *
import os
from megye import *

def fajlBeolvasas()->List[Varos]:
    ut:str="data/adatok.txt"
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    teljesut:str=os.path.join(alaput, ut)
    egysor:str=None
    egyseg:List[str]=[]
    varos:Varos=None
    varosok:List[Varos]=[]
    try:
        with open(teljesut,mode="r", encoding="utf-8") as file:
            for sor in file:
                egysor=sor.strip()
                egyseg=egysor.split("\t")
                varos = Varos()
                varos.nev=egyseg[0]
                varos.varosTipusa=egyseg[1]
                varos.megyeNeve=egyseg[2]
                varos.jaras=egyseg[3]
                varos.kisterseg=egyseg[4]
                varos.nepesseg=int(egyseg[5])
                varos.terulet=float(egyseg[6])
                varosok.append(varos)
            return varosok
    except FileNotFoundError as er:
        print(f"A fájlal valami nyűg van {er.filename}")
        return []

def fajlkiiras(varosok:List[Varos], fajlnev:str)->None:
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    alaput += "/output/"
    teljesut:str=os.path.join(alaput,fajlnev)
    try:
        with open(teljesut,mode="w",encoding="utf-8") as file:
            for varos in varosok:
                file.write(f"{varos}\n")
    except FileNotFoundError as er:
        print(f"A fájlal valami nyűg van {er.filename}")
        return []