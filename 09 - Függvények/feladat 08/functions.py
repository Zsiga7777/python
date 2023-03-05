from math import sqrt
def tavolsagSzamitas(a:float, b:float, c:float, d:float)->float:
    eredmeny:float=0
    eredmeny = sqrt( (c - a)**2 + (d - b)**2 )
    return eredmeny
