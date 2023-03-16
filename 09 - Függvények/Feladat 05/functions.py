def egyezes(szo1:str, szo2:str)->int:
    db:int=0
    hasznaltBetu:str=""
    for i in szo1:
        if(szo2.count(i) and hasznaltBetu.count(i) == 0 ):
            db += 1
            hasznaltBetu += i
    return db
