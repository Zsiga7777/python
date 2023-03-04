import datetime 
def kor(a:int)->int:
    kor:int=None
    datum = datetime.date.today()
    evszam = datum.year
    int(evszam)
    kor = evszam - a
    return kor