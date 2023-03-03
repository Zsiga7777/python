from functions import *
from kibe import *

szam1:float=None
szam2:float=None
eredmeny:float = None

szam1 = bekeres()
szam2 = bekeres()

eredmeny=osszeada(szam1, szam2)
kiiras (szam1, szam2, eredmeny, "+")