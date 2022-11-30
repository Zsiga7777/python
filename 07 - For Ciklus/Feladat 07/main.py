from os import system

szam1:int=None
szam2:int=None

print("Kérem a kezdő értéket:",end='')
szam1=int(input())

print("Kérem a végső értéket:",end='')
szam2=int(input())

system('cls')
if(szam1>szam2):
    for i in range(szam1, szam2, -1):
        print(i)
else:
    for i in range(szam2, szam1, -1):
        print(i)