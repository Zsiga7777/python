from os import system

szam:int=None

print("Kérek egy számot:",end='')
szam=int(input())

system('cls')

if (szam>0):
    print("A szám nagyobb, mint 0")
elif(szam<0):
    print("A szám kisebb, mint 0")
else:
    print("A szám 0")