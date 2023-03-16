def oraberSzamitas(oraSzam:int)->int:
    eredmeny:int=0
    fizetes:int = 1000
    eredmeny = oraSzam*fizetes
    if(oraSzam > 40):
        eredmeny = eredmeny + ((oraSzam-40)*500)
    return eredmeny
