from os import system

elsoSzam:int=None
masodikSzam:int=None
harmadikSzam:int=None
negyedikSzam:int=None
eredmeny:float=None

print("Kérem az első számot:",end='')
elsoSzam=int(input())

print("Kérem a második számot:",end='')
masodikSzam=int(input())

print("Kérem a harmadik számot:",end='')
harmadikSzam=int(input())

print("Kérem a negyedik számot:",end='')
negyedikSzam=int(input())

eredmeny=(elsoSzam+masodikSzam)/(harmadikSzam-negyedikSzam)

system('cls')

print(f"A végeredmény:{eredmeny}")