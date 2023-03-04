from kibe import *
from functions import *

nev:str = None
eletkor:int=None
szulEv :int = None

nev = nevbekeres()
szulEv = szuletesBekeres()
eletkor =kor(szulEv)

kiiras(nev, eletkor)
