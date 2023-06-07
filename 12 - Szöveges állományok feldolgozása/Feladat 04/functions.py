from varos import *
from typing import *
from megye import *

def megyeszekhelyKereses(varosok:List[Varos])->List[Varos]:
    megyeszekhelyek:List[Varos]=[]
    for varos in varosok:
        if (varos.varosTipusa == "megyeszékhely megyei jogú város"):
            megyeszekhelyek.append(varos)
    return megyeszekhelyek

def nepessegKereses(varosok:List[Varos])->List[Varos]:
    megfeleloVarosok:List[Varos]=[]
    for varos in varosok:
        if(int(varos.nepesseg) >=50000 and int(varos.nepesseg) <=100000):
            megfeleloVarosok.append(varos)
    return megfeleloVarosok

def teruletKereses(varosok:List[Varos])->List[Varos]:
    megfeleloVarosok:List[Varos]=[]
    for varos in varosok:
        if(float(varos.terulet) > 200 ):
            megfeleloVarosok.append(varos)
    return megfeleloVarosok

def megyeKereses(varosok:List[Varos], megye:str)->List[Varos]:
    megfeleloVarosok:List[Varos]=[]
    for varos in varosok:
        if(varos.megyeNeve == megye):
            megfeleloVarosok.append(varos)
    return megfeleloVarosok