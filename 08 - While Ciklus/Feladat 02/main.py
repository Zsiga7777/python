nev:str=None
szam:int=None

print("Kérem a nevét:", end='')
nev=str(input().strip())
szam=nev.count()
print(szam)

while (nev.isalnum() and szam <=2):
    szam = 0
    print("Kérem a nevét:", end='')
    nev=str(input().strip())
    szam=nev.count()

print(f"Üdvözlöm {nev} !")