from os import system

elsoSzam:int=None
masodikSzam:int=None
eredmeny:int=None

print("Kérem az első számot:",end='')
elsoSzam =int(input())

print("Kérem a második számot:",end='')
masodikSzam =int(input())

eredmeny= elsoSzam + masodikSzam

system('cls')

print(f"Az eredmény: {eredmeny}")