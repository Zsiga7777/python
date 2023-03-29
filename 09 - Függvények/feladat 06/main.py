from functions import *
from kibe import *

celMertek:str = None
fok:float = None
eredmeny:int = None

celMertek = bekeresMertekegyseg()
fok = bekeresSzam()
eredmeny = fokKonvert(fok, celMertek)

kiiras(fok,eredmeny,celMertek)