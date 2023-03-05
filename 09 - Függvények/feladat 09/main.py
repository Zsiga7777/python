from functions import *
from kibe import *

huf:float =None
eur:float=None
deviza:str=None
eredmeny:float = None

deviza = bekeresSzoveg()
huf = bekeresSzam()
eredmeny = devziaKonvert(huf, deviza)
eur = euroKonvert(eredmeny, deviza)

kiiras(huf, eredmeny, eur, deviza)