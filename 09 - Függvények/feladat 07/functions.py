import random

def randomSzam()->list:
    a :list = []
    for i in range (1, 11, 1):
        a.append(random.randint(0, 10000))
    return a

def osszeadas(a:list)->int:
    osszeg:int=0
    for i in range(0, 10, 1):
        osszeg += a[i]
    return osszeg

def melyikANagyobb (a:int, b:int)->str:
    nagyobb:str=None
    if(a==b):
        nagyobb = "Egyenlőek"
    elif(a > b):
        nagyobb ="Első"
    else:
        nagyobb = "Második"
    return nagyobb
