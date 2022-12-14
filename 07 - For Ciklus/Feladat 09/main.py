from os import system

kezdo:int=None
vegso:int=None

print("Kérem a kezdő értéket:",end='')
kezdo=int(input().strip())

print("Kérem a végső értéket:",end='')
vegso=int(input().strip())

system('cls')

if(kezdo%2):
    kezdo -=1

for i in range(kezdo, vegso-1, -2):
    print(i)