from os import system

elsoSzam:int=None
masodikSzam:int=None
harmadikSzam:int=None
eredmeny:int=None

print("Kérem az első számot:",end='')
elsoSzam=int(input())

print("Kérem a második számot:",end='')
masodikSzam=int(input())

print("Kérem a harmadik számot:",end='')
harmadikSzam=int(input())

eredmeny=(elsoSzam - masodikSzam)*harmadikSzam

system('cls')

print(f"A cégeredmény:{eredmeny}")