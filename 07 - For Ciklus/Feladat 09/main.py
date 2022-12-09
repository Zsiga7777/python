from os import system

kezdo:int=None
vegso:int=None

print("Kérem a kezdő értéket:",end='')
kezdo=int(input().strip())

print("Kérem a végső értéket:",end='')
vegso=int(input().strip())

system('cls')

if(kezdo>vegso):
    for i in range(kezdo, vegso+1, -1):
        if(i %2 == 0):
            print(i)
else:
    for i in range(vegso, kezdo+1, -1):
         if(i %2 == 0):
            print(i)