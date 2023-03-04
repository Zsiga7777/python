from functions import *
from kibe import *

szam1:float=None
szam2:float=None
eredmeny:float = None

szam1 = bekeres()
szam2 = bekeres()

eredmeny=osszeadas(szam1, szam2)
kiiras (szam1, szam2, eredmeny, "+")

eredmeny=kivonas(szam1, szam2)
kiiras (szam1, szam2, eredmeny, "-")

eredmeny=szorzas(szam1, szam2)
kiiras (szam1, szam2, eredmeny, "*")

eredmeny=osztas(szam1, szam2)
kiiras (szam1, szam2, eredmeny, "/")