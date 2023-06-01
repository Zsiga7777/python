from roplabdas import *
from typing import *
from nemzetiseg import *

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

def nemzetisegSzamlalo(roplabdasok:List[Roplabdas])->Set[Nemzetiseg]:
    nemzetisegek:Set(Nemzetiseg)
    for roplabdas in roplabdasok:
        nemzetisegek
