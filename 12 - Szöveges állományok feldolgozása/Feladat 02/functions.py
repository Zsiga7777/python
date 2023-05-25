from konyv import *
from typing import *

def temaKereses(konyvek:List[Konyv])->List[Konyv]:
    infosKonyvek:List[Konyv]=[]
    for konyv in konyvek:
        if(konyv.tema == "informatika"):
            infosKonyvek.append(konyv)
    return infosKonyvek

def evjaratSzamitas(konyvek:List[Konyv])->List[Konyv]:
    megfeleloEvjarat:List[Konyv]=[]
    for konyv in konyvek:
        if(int(konyv.kiadvasiEv) >=1900 and int(konyv.kiadvasiEv) <2000):
            megfeleloEvjarat.append(konyv)
    return megfeleloEvjarat
