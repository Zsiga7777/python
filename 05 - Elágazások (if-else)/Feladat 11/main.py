from os import system

szam:int=None

print("Kérek egy számot:",end='')
szam=int(input())

system('cls')

if ( szam%2 == 0 and szam>0 and szam%5 == 0 ):
    print("A szám osztható 5-tel, páros és pozitív")

elif ( szam%2 != 0 and szam<0 and szam%5 != 0 ):
    print("A szám nem osztható 5-tel, páratlan és negatív")

elif ( szam%2 != 0 and szam>0 and szam%5 == 0 ):
    print("A szám osztható 5-tel, páratlan és pozitív")
elif ( szam%2 != 0 and szam<0 and szam%5 == 0 ):
    print("A szám osztható 5-tel, páratlan és negatív")
elif ( szam%2 != 0 and szam>0 and szam%5 != 0 ):
    print("A szám nem osztható 5-tel, páratlan és pozitív")

elif ( szam%2 == 0 and szam<0 and szam%5 != 0 ):
    print("A szám nem osztható 5-tel, páros és negatív")
elif ( szam%2 == 0 and szam>0 and szam%5 != 0 ):
    print("A szám nem osztható 5-tel, páros és pozitív")
elif ( szam%2 == 0 and szam<0 and szam%5 == 0 ):
    print("A szám osztható 5-tel, páros és negatív")
