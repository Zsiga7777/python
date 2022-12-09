from os import system

kezdo:int=None
vegso:int=None
eredmeny1:int=0
eredmeny2:int=1

print("Kérem a kezdő értéket:",end='')
kezdo=int(input().strip())

print("Kérem a végső értéket:",end='')
vegso=int(input().strip())

system('cls')
if(kezdo<vegso):
    for i in range(kezdo, vegso+1, 1):
        eredmeny1 = eredmeny1+i
        eredmeny2= eredmeny2*i
    print(f"Az összeg {eredmeny1}")
    print(f"A szorzat {eredmeny2}")

else:
    for i in range(vegso, kezdo+1, 1):
        eredmeny1 = eredmeny1+i
        eredmeny2= eredmeny2*i
    print(f"Az összeg {eredmeny1}")
    print(f"A szorzat {eredmeny2}")
