from os import system

kezdo:int=None
vegso:int=None
darab:int=0
atlag:float=0

print("Kérem a kezdő számot:", end='')
kezdo=int(input().strip())

print("Kérem a végső számot:", end='')
vegso=int(input().strip())


for i in range(kezdo, vegso+1, 1):
        atlag = atlag + i
        darab+=1

atlag = atlag/darab


system('cls')

print(f"A számok átlaga: {atlag} ")