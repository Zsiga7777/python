from functions import *
from kibe import *
from os import system

nevek:str=None
orak:int=None
fizetesek:int=None


system('cls')
munkasSzam = bekeresMunkasSzam()
nevek = nevekBekeres(munkasSzam)
orak= szamokBekeres(munkasSzam)
fizetesek = oraberSzamitas(orak, munkasSzam)
system('cls')
kiiras(nevek, orak, fizetesek, munkasSzam)