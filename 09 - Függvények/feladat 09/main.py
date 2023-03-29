from functions import *
from kibe import *

huf:float =None
eur:float=None

deviza:str=bekeresSzoveg()
eredmeny:float = None

huf = bekeresSzam()
eredmeny = devziaKonvert(huf, deviza)
eur = euroKonvert(eredmeny, deviza)

kiiras(huf, eredmeny, eur, deviza)