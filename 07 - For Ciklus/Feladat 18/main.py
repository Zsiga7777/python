from os import system

kezdo:int=None
vegso:int=None
darab:int=1
osszeg:int=0

print("Kérem a kezdő számot:", end='')
kezdo=int(input().strip())

print("Kérem a végső számot:", end='')
vegso=int(input().strip())


for i in range(kezdo, vegso+1, 2):
        osszeg = osszeg+i
        
for i in range(kezdo+1, vegso+1, 2):
        osszeg = osszeg+(i*-1)
print(f"{osszeg}")