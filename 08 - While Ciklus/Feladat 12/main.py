megtakaritas:int = None
megtakaritasMasolat:str = None
honapokSzama:int=0

while (megtakaritas == None or megtakaritas < 0 or megtakaritas > 100000):
    print("Kérek egy megtakarított összeget:", end='')
    megtakaritas = input()
    megtakaritasMasolat = megtakaritas.replace(".","").replace("-","")
    if(megtakaritasMasolat.isnumeric()):
        megtakaritas = int(megtakaritas)
    else:
        megtakaritas = None


while (megtakaritas < 100000):
    megtakaritas = megtakaritas * 1.02
    honapokSzama +=1

print(f"{honapokSzama} hónap alatt lesz 100000 Ft a megtakarítás")
