from os import system

kezdo:int=None
vegso:int=None
paratlanOsszeg:int=0
parosOsszeG:int=0
atlag1:float=0
atlag2:float=0
darab1:int=0
darab2:int=0

print("Kérem a kezdő számot:", end='')
kezdo=int(input().strip())

print("Kérem a végső számot:", end='')
vegso=int(input().strip())

if (kezdo>vegso):
    for i in range(vegso, kezdo+1, 1):
        if(i % 2 ==0):
            parosOsszeG = parosOsszeG + i
            darab1+=1
        else:
            paratlanOsszeg = paratlanOsszeg + i
            darab2+=1
else:
    for i in range(kezdo, vegso+1, 1):
        if (i %2 ==0):
            parosOsszeG = parosOsszeG + i
            darab1+=1
        else:
            paratlanOsszeg = paratlanOsszeg + i
            darab2+=1

atlag1 = parosOsszeG/darab1
atlag2 = paratlanOsszeg/darab2

system('cls')

print(f"A páros átlaga: {atlag1} \n A páratlan számok átlaga: {atlag2}")

