from os import system

elsoSzam:int=None
masodikSzam:int=None


print("Kérem az első számot:",end='')
elsoSzam=int(input())

print("Kérem a második számot:",end='')
masodikSzam=int(input())


system('cls')

if ( elsoSzam > masodikSzam ):
    print(f" Az első szám a nagyobb, {elsoSzam}")
elif( elsoSzam < masodikSzam ):
    print(f"A második szám nagyobb, {masodikSzam}")
else:
    print("A két szám egyenlő")