def egyezes(a:str, b:str)->int:
    db:int=0
    betuElsoSzo:str=None
    betuMasodikSzo:str=None
    for i in range (0, len(a), 1):
        betuElsoSzo = a[i]
        for j in range (0, len(b), 1):
            betuMasodikSzo = b[j]
            if(betuElsoSzo == betuMasodikSzo):
                db +=1
    return db
