from os import system

szam1:int=None
szam2:int=None
osszeg1:int=0
osszeg2:int=0

print("Kérem a kezdő értéket:",end='')
szam1=int(input().strip())

print("Kérem a végső értéket:",end='')
szam2=int(input().strip())

system('cls')
if(szam1<szam2):
    for i in range(szam1, szam2+1):
        if(i%2 ==0):
            osszeg1 = osszeg1+i
        else:
            osszeg2 = osszeg2+i
else:
    for i in range(szam2, szam1+1):
        if(i%2 ==0):
            osszeg1 = osszeg1+i
        else:
            osszeg2 = osszeg2+i
if (osszeg1 > osszeg2):
    print(f"A páros számokoknak nagyobb az összege, {osszeg1}")
elif(osszeg2 > osszeg1):
    print(f"A páratlan számoknak nagyobb az összege, {osszeg2}")
else:
    print(f"egyenlő az összegük, {osszeg1}")