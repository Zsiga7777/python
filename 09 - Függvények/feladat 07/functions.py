import random

def randomSzam()->list:
    a :list = []
    for i in range (1, 11, 1):
        a.append(random.randint(0, 10000))
    return a

def osszeadas(lista:list)->int:
    osszeg:int=0
    for i in range(0, 10, 1):
        osszeg += lista[i]
    return osszeg

def melyikANagyobb (osszeg1:int, osszeg2:int)->str:
    nagyobb:str=None
    if(osszeg1==osszeg2):
        nagyobb = "Egyenlőek"
    elif(osszeg1 > osszeg2):
        nagyobb ="Első"
    else:
        nagyobb = "Második"
    return nagyobb
