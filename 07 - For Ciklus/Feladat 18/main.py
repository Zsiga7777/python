from os import system

kezdo:int=None
vegso:int=None
darab:int=1
osszeg:int=0

print("Kérem a kezdő számot:", end='')
kezdo=int(input().strip())

print("Kérem a végső számot:", end='')
vegso=int(input().strip())

if (kezdo<vegso):
    for i in range(kezdo, vegso+1, 1):
        if(darab % 2==0):
            osszeg = osszeg-i
            darab +=1
        else:
            osszeg = osszeg+ i
            darab +=1
else:
    for i in range(vegso, kezdo+1 , 1):
        if(darab % 2==0):
            osszeg = osszeg-i
            darab +=1
        else:
            osszeg = osszeg+ i
            darab +=1
print(f"{osszeg}")