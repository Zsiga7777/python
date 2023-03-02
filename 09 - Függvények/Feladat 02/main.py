nev:str = None

def nevbekeres(betu_e:bool)->str:
    while(betu_e == False or len(ideig) < 2):
        print("Kérek egy nevet:", end='')
        ideig:str=input().strip()
        if(ideig.isalpha()):
            betu_e = True
    return ideig

nev = nevbekeres(False)
print(f"Üdvözlöm {nev}")