from os import system

elsoSzam:int=None
masodikSzam:int=None
harmadikSzam:int=None


print("Kérem az első számot:",end='')
elsoSzam=int(input())

print("Kérem a második számot:",end='')
masodikSzam=int(input())

print("Kérem a harmadik számot:",end='')
harmadikSzam=int(input())

system('cls')

if ( elsoSzam > masodikSzam and elsoSzam > harmadikSzam and masodikSzam > harmadikSzam):
    print(f" {harmadikSzam}, {masodikSzam}, {elsoSzam}")
elif ( elsoSzam > masodikSzam and elsoSzam > harmadikSzam and masodikSzam < harmadikSzam):
    print(f" {masodikSzam}, {harmadikSzam}, {elsoSzam}")

elif ( masodikSzam > elsoSzam and elsoSzam > harmadikSzam and masodikSzam > harmadikSzam):
    print(f" {harmadikSzam}, {elsoSzam}, {masodikSzam}")
elif ( masodikSzam > elsoSzam and elsoSzam < harmadikSzam and masodikSzam > harmadikSzam):
    print(f" {elsoSzam}, {harmadikSzam}, {masodikSzam}")

elif ( harmadikSzam > elsoSzam and harmadikSzam > masodikSzam and elsoSzam > masodikSzam):
    print(f" {masodikSzam}, {elsoSzam}, {harmadikSzam}")
elif ( harmadikSzam > elsoSzam and harmadikSzam > masodikSzam and elsoSzam < masodikSzam):
    print(f" {elsoSzam}, {masodikSzam}, {harmadikSzam}")
else:
    print(f"{elsoSzam},{masodikSzam},{harmadikSzam}")