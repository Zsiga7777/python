bekertSzam:int=None
bekertSzamMasolat:str=None

while (bekertSzam == None or bekertSzam < 100 or bekertSzam > 999):
    print("Kérek egy 3 jegyű számot: ", end='')
    bekertSzam = input()
    bekertSzamMasolat = bekertSzam.replace(".", "").replace("-","")
    if(bekertSzamMasolat.isnumeric()):
        bekertSzam = int(bekertSzam)
    else:
        bekertSzam = None

if(bekertSzam % 7 == 0):
    print("A szám osztható 7-tel")
else:
    print("A szám nem osztható 7-tel")