from functions import *
from kibe import *

x1:float = None
x2:float = None
y1:float = None
y2:float = None
tavolsag:float = None

x1 = bekeres()
y1 = bekeres()
x2 = bekeres()
y2 = bekeres()

tavolsag = tavolsagSzamitas(x1,y1,x2,y2)

kiiras(tavolsag)