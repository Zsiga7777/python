from konyv import *
from typing import *
import os
def konyvBeolvasas()->List[Konyv]:
    fileName:str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)
    oneLine:str = None
    data:list[str]=[]
    konyvek:List[Konyv]=[]
    konyv:Konyv=None

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data=oneLine.split("\t")
                konyv= Konyv()
                konyv.vezeteknev=data[0]
                konyv.keresztnev= data[1]
                konyv.szuletesiDatum= data[2]
                konyv.cim= data[3]
                konyv.iSBN=data[4]
                konyv.kiado= data[5]
                konyv.kiadvasiEv= data[6]
                konyv.ar= data[7]
                konyv.tema=data[8]
                konyv.oldalszam= data[9]
                konyv.honorarium= data[10]
                konyvek.append(konyv)
        return konyvek
            
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []
    
def fajlKiiras(konyvek:List[Konyv],fajlNev:str)->None:
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    alaput += "/output/"
    teljesUt:str=os.path.join(alaput,fajlNev)
    try:
        with open(teljesUt,encoding="utf-8",mode="w",) as file:
            for konyv in konyvek:
                file.write(f"{konyv}\n")
        
    except FileNotFoundError as ex:
        print(f"{ex.filename} fájlal valami nyűg van")