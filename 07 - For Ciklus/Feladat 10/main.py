from os import system

kezdo:int=None
vegso:int=None
osszeg:int=0
szorzat:int=1

print("Kérem a kezdő értéket:",end='')
kezdo=int(input().strip())

print("Kérem a végső értéket:",end='')
vegso=int(input().strip())

system('cls')
for i in range(kezdo, vegso+1, 1):
    osszeg = osszeg+i
    szorzat= szorzat*i
print(f"Az összeg {osszeg}")
print(f"A szorzat {szorzat}")
