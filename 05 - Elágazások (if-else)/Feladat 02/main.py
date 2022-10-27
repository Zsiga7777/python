from os import system

szam:int=None

print("Kérek egy számot:",end='')
szam=int(input())

system('cls')

if (szam>=0):
    print("A szám pozitív")
else:
    print("A szám negatív")