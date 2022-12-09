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
if (kezdo<vegso):
    for i in range(kezdo, vegso+1, 1):
        if(i%2):
            eredmeny1 = eredmeny1+i
        else:
            eredmeny2 = eredmeny2*i
else:
    for i in range(vegso, kezdo+1, 1):
        if(i%2):
            eredmeny1 = eredmeny1+i
        else:
            eredmeny2 = eredmeny2*i
print(f"A páros számok összeg: {eredmeny1} \n A páratlan számok szorzata: {eredmeny2}")