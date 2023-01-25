szam:float=None
osszeg:float=0
db:int=0

while (osszeg == None or osszeg<100):
    print("Kérek egy új számot: ", end='')
    szam = int(input())
    db +=1
    osszeg = osszeg +szam
    print(f"Jelenleg az összeg {osszeg}, és {db} bevitelnél tart.")