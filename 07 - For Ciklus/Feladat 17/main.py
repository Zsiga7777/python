from os import system

kezdo:int=None
vegso:int=None
darab:int=0
atlag:float=0

print("Kérem a kezdő számot:", end='')
kezdo=int(input().strip())

print("Kérem a végső számot:", end='')
vegso=int(input().strip())

if (kezdo>vegso):
    for szam in range(vegso, kezdo+1):
            atlag = atlag + szam
            darab+=1
else:
    for szam in range(kezdo, vegso+1):
            atlag = atlag + szam
            darab+=1

atlag = atlag/darab


system('cls')

print(f"A számok átlaga: {atlag} ")