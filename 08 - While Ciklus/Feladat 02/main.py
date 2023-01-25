nev:str=None
szam:int=None

while (nev!= None and szam <=2):
    szam = 0
    print("Kérem a nevét:", end='')
    nev=str(input().strip())
    szam=nev.__len__()

print(f"Üdvözlöm {nev} !")