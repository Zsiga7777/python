from os import system

szam1:int=None
szam2:int=None
eredmeny1:int=0
eredmeny2:int=1

print("Kérem a kezdő értéket:",end='')
szam1=int(input().strip())

print("Kérem a végső értéket:",end='')
szam2=int(input().strip())

system('cls')
if(szam1<szam2):
    for i in range(szam1, szam2+1):
        eredmeny1 = eredmeny1+i
        eredmeny2= eredmeny2*i
    print(f"Az összeg {eredmeny1}")
    print(f"A szorzat {eredmeny2}")

else:
    for i in range(szam2, szam1+1):
        eredmeny1 = eredmeny1+i
        eredmeny2= eredmeny2*i
    print(f"Az összeg {eredmeny1}")
    print(f"A szorzat {eredmeny2}")
