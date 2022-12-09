from os import system

kezdo:int=None
vegso:int=None
darab1:int=0

print("Kérem a kezdő értéket:",end='')
kezdo=int(input().strip())

print("Kérem a végső értéket:",end='')
vegso=int(input().strip())

system('cls')
if(kezdo<vegso):
    for i in range(kezdo, vegso+1, 1):
        if(i%2 !=0 and i%3==0):
            darab1 = darab1+1
    for i in range(vegso, kezdo+1, 1):
        if(i%2 !=0 and i%3==0):
            darab1 = darab1+1
print(f"Összesen ennyi páratlan szám osztható 3-al: {darab1}")