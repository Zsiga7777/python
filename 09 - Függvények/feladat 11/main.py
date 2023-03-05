from functions import *
from kibe import *
from os import system

nev1:str=None
ora1:int=None
fizetes1:int=None

nev2:str=None
ora2:int=None
fizetes2:int=None

nev3:str=None
ora3:int=None
fizetes3:int=None

nev4:str=None
ora4:int=None
fizetes4:int=None

nev5:str=None
ora5:int=None
fizetes5:int=None

nev1 = bekeresNev()
ora1 = bekeresSzam()
fizetes1 = oraberSzamitas(ora1)

nev2 = bekeresNev()
ora2 = bekeresSzam()
fizetes2 = oraberSzamitas(ora2)

nev3 = bekeresNev()
ora3 = bekeresSzam()
fizetes3 = oraberSzamitas(ora3)

nev4 = bekeresNev()
ora4 = bekeresSzam()
fizetes4 = oraberSzamitas(ora4)

nev5 = bekeresNev()
ora5 = bekeresSzam()
fizetes5 = oraberSzamitas(ora5)

system('cls')

kiiras(ora1, fizetes1, nev1)
kiiras(ora2, fizetes2, nev2)
kiiras(ora3, fizetes3, nev3)
kiiras(ora4, fizetes4, nev4)
kiiras(ora5, fizetes5, nev5)
