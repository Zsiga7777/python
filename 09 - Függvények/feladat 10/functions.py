import random
from kibe import *
def randomSzam(min:int, max:int)->int:
    eredmeny:int=0
    eredmeny = random.randint(min, max)
    return eredmeny

def jatek(randomSzam:int)->int:
    db:int=0
    tipp:int=None
    while (tipp == None or tipp != randomSzam):
        tipp = bekeresSzam()
        db +=1
        if(tipp>randomSzam):
            print("A keresett szám kisebb")
        elif(tipp<randomSzam):
            print("A keresett szám nagyobb")
    return db
