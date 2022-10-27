from os import system

szam:int=None

print("Kérek egy számot:",end='')
szam=int(input())

system('cls')

if ( szam%2 == 0 and szam%3 != 0 ):
    print("BIZ")
elif ( szam%2 != 0 and szam%3 ==0 ):
    print("BAZ")
elif ( szam%2 == 0 and szam%3 ==0 ):
    print("ZIZI")
else:
    print("A szám nem osztható sem 2-vel, sem 3-al.")