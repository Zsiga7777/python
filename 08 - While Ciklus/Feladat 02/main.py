nev:str=None
betu_e :bool = True

while (nev == None or len(nev) <2 or betu_e == False):
    print("Kérem a nevét:", end='')
    nev=str(input().strip())
    betu_e = nev.isalpha()
    
print(f"Üdvözlöm {nev} !")