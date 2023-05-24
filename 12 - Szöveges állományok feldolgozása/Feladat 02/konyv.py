from  datetime import *
class Konyv(): 
    def __init__(self):
        super().__init__()
        self.vezeteknev:str=None
        self.keresztnev:str=None
        self.szuletesiDatum:str=None
        self.cim:str=None
        self.iSBN:int=0
        self.kiado:str=None
        self.kiadvasiEv:int=0
        self.ar:float=0
        self.tema:str=None
        self.oldalszam:int=0
        self.honorarium:float=0 
    
    def __str__(self) -> str:
        return f"{self.vezeteknev} {self.keresztnev} ({self.szuletesiDatum}) - {self.cim} ({self.iSBN}) {self.kiado} [{self.kiadvasiEv}] ár:{self.ar} Ft, témája:{self.tema}, oldaszáma:{self.oldalszam}, honoránium:{self.honorarium} Ft "