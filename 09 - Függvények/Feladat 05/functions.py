def egyezes(szo1:str, szo2:str)->int:
    db:int=0
    szo1Masolat:str=""
    szo2Masolat:str=""
    for i in szo1:
        if(szo1Masolat.count(i) == 0):
            szo1Masolat += i
    for i in szo2:
        if(szo2Masolat.count(i) == 0):
            szo2Masolat += i
    for i in szo1Masolat:
        db += szo2Masolat.count(i)
    return db
