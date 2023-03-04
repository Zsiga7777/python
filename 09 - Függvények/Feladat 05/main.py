from functions import *
from kibe import *

szo1:str = None
szo2:str = None
egyezesekSzama:int = None

szo1 = bekeres()
szo2 = bekeres()
egyezesekSzama = egyezes(szo1, szo2)

kiiras(egyezesekSzama)