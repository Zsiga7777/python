def oraberSzamitas(a:int)->int:
    eredmeny:int=0
    fizetes:int = 1000
    eredmeny = a*fizetes
    if(a > 40):
        eredmeny = eredmeny + ((a-40)*500)
    return eredmeny
