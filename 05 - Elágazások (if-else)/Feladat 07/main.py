from os import system

szam:int=None
eredmeny:int=None

print("Kérek egy számot:",end='')
szam=int(input())

eredmeny=szam%5

system('cls')

if (eredmeny==0):
    print("A szám osztható öttel")
else:
    print("A szám nem osztható öttel")