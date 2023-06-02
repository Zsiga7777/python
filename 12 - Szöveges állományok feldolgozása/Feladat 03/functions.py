from roplabdas import *
from typing import *
from atlagnalMagasabbak import *
from kibe import *

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

def atlagnalNagyobbak(roplabdasok:List[Roplabdas],atlagMagassag:float)->List[Atlagfelettiek]:
    magasabbak:List[Atlagfelettiek]=[]
    magasabb:Atlagfelettiek = Atlagfelettiek()
    for roplabdas in roplabdasok:
        if(atlagMagassag < roplabdas.magassag):
            magasabb.nev = roplabdas.nev
            magasabb.magassag = roplabdas.magassag
            magasabbak.append(magasabb)
    return magasabbak