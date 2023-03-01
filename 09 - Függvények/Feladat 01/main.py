szam1:int=6
szam2:int=9
eredmeny:float = 0

def osszeada (a:int, b:int)->int:
    osszeg:int= a+b
    return osszeg
def kivonas (a:int, b:int)->int:
    vegleges:int= a-b
    return vegleges
def szorzas (a:int, b:int)->int:
    szorzat:int= a*b
    return szorzat
def osztas (a:int, b:int)->float:
    vegleges:int= a/b
    return vegleges

eredmeny = osszeada(szam1, szam2)
print(f"Az összeadás eredménye:{eredmeny}")
eredmeny = kivonas(szam1, szam2)
print(f"A kivonás eredménye:{eredmeny}")
eredmeny = szorzas(szam1, szam2)
print(f"A szorzás eredménye:{eredmeny}")
eredmeny = osztas(szam1, szam2)
print(f"Az osztás eredménye:{eredmeny}")