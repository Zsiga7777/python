from os import system

szam1:int=None
szam2:int=None
eredmeny1:int=0

print("Kérem a kezdő értéket:",end='')
szam1=int(input().strip())

print("Kérem a végső értéket:",end='')
szam2=int(input().strip())

system('cls')
if(szam1<szam2):
    for i in range(szam1, szam2+1):
        if(i%3 ==0):
            eredmeny1 = eredmeny1+1
else:
    for i in range(szam2, szam1+1):
        if(i%3 ==0):
            eredmeny1 = eredmeny1+1
print(f"A számok darabszáma:{eredmeny1}")