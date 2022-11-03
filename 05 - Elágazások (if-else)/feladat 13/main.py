from os import system

szam:int=None

print("Kérek egy számot:",end='')
szam=int(input())

system('cls')

if ( szam >= 0 and szam <= 9 ):
    print("A szám egyjegyű")

elif ( szam >= 10 and szam <= 99 ):
    print("A szám kétjegyű")

elif ( szam >= 100 and szam <= 999 ):
    print("A szám háromjegyű")

else:
    print("A szám nem 0 és 1000 között van")
