from functions import *
from kibe import *

lista1:str = ""
lista2:str = ""
osszeg1:int= None
osszeg2:int= None
eredmeny:str=None

lista1 = randomSzam()
lista2 = randomSzam()
osszeg1 = osszeadas(lista1)
osszeg2 = osszeadas(lista2)
eredmeny = melyikANagyobb(osszeg1, osszeg2)

kiiras(lista1,lista2,osszeg1,osszeg2,eredmeny)