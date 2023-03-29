from math import sqrt

def tavolsagSzamitas(x1:float, x2:float, y1:float, y2:float)->float:
    eredmeny:float=0
    eredmeny = sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
    return eredmeny
