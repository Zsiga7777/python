nev:str=None
szam:int=0
betu_e :bool = True

while (nev == None or szam <=1 or betu_e == False):
    szam = 0
    print("Kérem a nevét:", end='')
    nev=str(input().strip())
    szam=nev.__len__()
    betu_e = nev.isalpha()
    
print(f"Üdvözlöm {nev} !")