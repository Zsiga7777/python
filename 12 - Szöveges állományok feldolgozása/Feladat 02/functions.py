from konyv import *
from typing import *

def temaKereses(konyvek:List[Konyv])->List[Konyv]:
    infosKonyvek:List[Konyv]=[]
    for konyv in konyvek:
        if(konyv.tema == "informatika"):
            infosKonyvek.append(konyv)
    return infosKonyvek