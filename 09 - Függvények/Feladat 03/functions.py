import datetime 
def kor(evszam:int)->int:
    kor:int=None
    kor = datetime.date.today().year - evszam
    return kor