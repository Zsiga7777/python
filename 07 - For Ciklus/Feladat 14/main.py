from os import system

kezdo:int=None
vegso:int=None
osszeg1:int=0
osszeg2:int=0

print("Kérem a kezdő értéket:",end='')
kezdo=int(input().strip())

print("Kérem a végső értéket:",end='')
vegso=int(input().strip())

system('cls')
for i in range(kezdo, vegso+1, 1):
    if(i%5 ==0):
        osszeg1 = osszeg1+i
    elif (i % 7==0):
        osszeg2 = osszeg2+i

if (osszeg1 > osszeg2):
    print(f"Az öttel osztható számok összege a nagyobb, {osszeg1}")
elif(osszeg2 > osszeg1):
    print(f"A héttel osztható számok összege a  nagyobb, {osszeg2}")
else:
    print(f"egyenlő az összegük, {osszeg1}")