import random
from kibe import *
def randomSzam(a:int, b:int)->int:
    eredmeny:int=0
    eredmeny = random.randint(a, b)
    return eredmeny

def jatek(a:int)->int:
    db:int=0
    tipp:int=None
    while (tipp == None or tipp != a):
        tipp = bekeresSzam()
        db +=1
        if(tipp>a):
            print("A keresett szám kisebb")
        elif(tipp<a):
            print("A keresett szám nagyobb")
    return db
