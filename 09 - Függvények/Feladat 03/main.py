nev:str = None
eletkor:int=None

def nevbekeres(betu_e:bool)->str:
    while(betu_e == False or len(ideig) < 2):
        print("Kérek egy nevet:", end='')
        ideig:str=input().strip()
        if(ideig.isalpha()):
            betu_e = True
    return ideig

def szuletesBekeres(szam_e:bool)->int:
    while(szam_e == False or szuletesidattum <1920 or szuletesidattum > 2023):
        print("Kérek a születési évét:", end='')
        ideig:str=input().strip()
        ideigmasolat= ideig.replace("-", "").replace(".", "")
        if(ideigmasolat.isnumeric()):
            szam_e = True
            szuletesidattum:int = int(ideig)
    return szuletesidattum

nev = nevbekeres(False)
eletkor =2023- szuletesBekeres(False)
print(f"{nev}, ön az idén {eletkor+1} éves lesz")