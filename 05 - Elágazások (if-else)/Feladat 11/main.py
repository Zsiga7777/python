from os import system

szam:int=None

print("Kérek egy számot:",end='')
szam=int(input())

system('cls')

if(szam%2 ==0):
    print("A szám páros")
elif(szam%2 !=0):
    print("A szám páratlan")

if (szam>=0):
    print("A szám pozitív")
elif (szam<0):
    print("A szám negatív")

if (szam%5==0):
    print("A szám osztható 5-tel")
elif(szam%5!=0):
    print("A szám nem osztható 5-tel")