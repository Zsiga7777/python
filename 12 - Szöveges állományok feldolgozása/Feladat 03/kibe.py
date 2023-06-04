from roplabdas import *
from typing import *
import os
def fajlOlvasas()->List[Roplabdas]:
    fajlnev:str= "data/adatok.txt"
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    teljesut:str=os.path.join(alaput,fajlnev)
    roplabdasok:List[Roplabdas]=[]
    egysor:str=None
    egyseg:List[str]=[]
    roplabdas:Roplabdas= None
    try:
        with open(teljesut,mode="r",encoding="utf-8") as file:
            for line in file:
                egysor =line.strip()
                egyseg=egysor.split("\t")
                roplabdas = Roplabdas()
                roplabdas.nev = egyseg[0]
                roplabdas.magassag = int(egyseg[1])
                roplabdas.poszt = egyseg[2]
                roplabdas.nemzetiseg = egyseg[3]
                roplabdas.csapat = egyseg[4]
                roplabdas.orszag = egyseg[5]
                roplabdasok.append(roplabdas)
        return roplabdasok
    except FileNotFoundError as er:
        print(f"A fájlal valami nyűg van {er.filename}")
        return []
                
def fajlKiiras(roplabdasok:List, fajlnev:str)->None:
    alapUt:str=os.path.dirname(os.path.abspath(__file__))
    alapUt += "/output/"
    teljesUt:str=os.path.join(alapUt, fajlnev)
    try:
        with open(teljesUt, encoding="utf-8", mode="w") as file:
            for roplabdas in roplabdasok:
                file.write(f"{roplabdas}\n")
    except FileNotFoundError as er:
        print(f"Valami nyűg van a {er.filename}")