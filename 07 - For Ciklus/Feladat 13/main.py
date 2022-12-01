from os import system

szam1:int=None
szam2:int=None
db1:int=0
db2:int=0

print("Kérem a kezdő értéket:",end='')
szam1=int(input())

print("Kérem a végső értéket:",end='')
szam2=int(input())

system('cls')
for i in range(szam1, szam2):
    if(i%2 ==0):
        db1 = db1+i
    else:
        db2 = db2+i
if (db1 > db2):
    print(f"A páros számokoknak nagyobb az összege, {db1}")
elif(db2 > db1):
    print(f"A páratlan számoknak nagyobb az összege, {db2}")
else:
    print(f"egyenlő az összegük, {db1}")