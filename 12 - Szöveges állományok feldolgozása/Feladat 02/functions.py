from konyv import *
from typing import *

def temaKereses(konyvek:List[Konyv],tema:str)->List[Konyv]:
    infosKonyvek:List[Konyv]=[]
    for konyv in konyvek:
        if(konyv.tema == tema):
            infosKonyvek.append(konyv)
    return infosKonyvek

def evjaratSzamitas(konyvek:List[Konyv], start:int, end:int)->List[Konyv]:
    megfeleloEvjarat:List[Konyv]=[]
    for konyv in konyvek:
        if(int(konyv.kiadvasiEv) >=start and int(konyv.kiadvasiEv) <end):
            megfeleloEvjarat.append(konyv)
    return megfeleloEvjarat

def konyvRendezes(konyvek:List[Konyv])->None:
    listaHossz:int= len(konyvek)
    nagyobb:Konyv=None
    for i in range(0, listaHossz -1,1):
        for j in range(i+1,listaHossz,1):
            if(konyvek[j].oldalszam > konyvek[i].oldalszam ):
                nagyobb = konyvek[i]
                konyvek[i] = konyvek[j]
                konyvek[j] = nagyobb 