from os import system

kezdo:int=None
vegso:int=None
eredmeny1:int=0

print("Kérem a kezdő értéket:",end='')
kezdo=int(input().strip())

print("Kérem a végső értéket:",end='')
vegso=int(input().strip())

system('cls')
if(kezdo<vegso):
    for i in range(kezdo, vegso+1, 1):
        if(i%3 ==0):
            eredmeny1 = eredmeny1+1
else:
    for i in range(vegso, kezdo+1, 1):
        if(i%3 ==0):
            eredmeny1 = eredmeny1+1
print(f"A számok darabszáma:{eredmeny1}")