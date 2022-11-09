from os import system

szam:int=None

print("Kérek egy számot:",end='')
szam=int(input())

system('cls')

if ( (szam>10 and szam<20) or (szam<-10 and szam>-20)):
    print("A szám a megadott határértékek(-10:-20 vagy 10:20 tartomány) közöztt van")

else:
    print("A szám nincs a megadott határértékek(-10:-20 vagy 10:20 tartomány) között")