from functions import *
from kibe import *

elsoSzam:int=None
masodikSzam:int = None
szamitogepRandomSzam:int=None
tippekSzama:int=None

elsoSzam = randomSzam(0, 9)
masodikSzam = randomSzam(40,50)
szamitogepRandomSzam =randomSzam(elsoSzam, masodikSzam)
tippekSzama = jatek(szamitogepRandomSzam)

kiiras(szamitogepRandomSzam, tippekSzama)