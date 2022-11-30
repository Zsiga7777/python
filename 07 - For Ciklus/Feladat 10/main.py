from os import system

szam1:int=None
szam2:int=None
eredmeny1:int=0
eredmeny2:int=1

print("Kérem a kezdő értéket:",end='')
szam1=int(input())

print("Kérem a végső értéket:",end='')
szam2=int(input())

system('cls')
for i in range(szam1, szam2):
    eredmeny1 = eredmeny1+i
print(f"Az összeg {eredmeny1}")
for i in range(szam1, szam2):
    eredmeny2 = eredmeny2*i
print(f"A szorzat {eredmeny2}")
