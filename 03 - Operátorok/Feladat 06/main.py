from os import system

elsoSzam:float=None
masodikSzam:float=None
harmadikSzam:int=None
eredmenyResz:float=None
eredmeny:float=None

print("Kérem az első számot:",end='')
elsoSzam=float(input())

print("Kérem a második számot:",end='')
masodikSzam=float(input())

print("Kérem a harmadik számot:",end='')
harmadikSzam=int(input())

eredmenyResz=(elsoSzam+0.5)*(masodikSzam-0.7)
eredmeny=eredmenyResz%harmadikSzam

system('cls')

print(f"Az osztás eredménye:{eredmeny:1.2f}")


