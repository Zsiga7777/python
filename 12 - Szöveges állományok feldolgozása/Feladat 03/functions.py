from roplabdas import *
from typing import *
from atlagnalMagasabbak import *
from kibe import *
from atlagAlattiak import *

def posztKereses(roplabdasok:List[Roplabdas], poszt:str)->List [Roplabdas]:
    utok:List[Roplabdas]=[]
    for roplabdas in roplabdasok:
        if(roplabdas.poszt == poszt):
            utok.append(roplabdas)

    return utok

def magassagKereses(roplabdasok:List[Roplabdas])->None:
    db:int=len(roplabdasok)
    nagyobb:List[Roplabdas]= []
    for i in range(0, db-1,1):
        for j in range (i+1,db,1 ):
            if(roplabdasok[i].magassag > roplabdasok[j].magassag):
                nagyobb = roplabdasok[i]
                roplabdasok[i]= roplabdasok[j]
                roplabdasok[j] = nagyobb

def atlagmagassag(roplabdasok:List[Roplabdas])->float:
    osszes:float=0
    db:int=0
    for roplabdas in roplabdasok:
        osszes += roplabdas.magassag
        db +=1
    return osszes/db

def atlaghozKepest(roplabdasok:List[Roplabdas],atlagMagassag:float, valaszto:str)->List:
    eredmenyek:List[Atlagfelettiek]=[]
    eredmeny:Atlagfelettiek = None
    
    if(valaszto == "nagyobb"):
        for roplabdas in roplabdasok:
            if(atlagMagassag < roplabdas.magassag):
                eredmeny = Atlagfelettiek()
                eredmeny.nev = roplabdas.nev
                eredmeny.magassag = roplabdas.magassag
                eredmenyek.append(eredmeny)
        
        return eredmenyek
    else:
        for roplabdas in roplabdasok:     
            if(roplabdas.magassag < atlagMagassag):
                eredmeny = AtlgaAlattiak()
                eredmeny.nev = roplabdas.nev
                eredmeny.magassag = roplabdas.magassag
                eredmenyek.append(eredmeny)
        
        return eredmenyek

def atlagAlattiKulonbseg(atlagAlattiak:List[AtlgaAlattiak], atlagmagassag:float)->List[AtlgaAlattiak]:
    for roplabdas in atlagAlattiak:
        roplabdas.kulonbseg = atlagmagassag-roplabdas.magassag
    return atlagAlattiak
