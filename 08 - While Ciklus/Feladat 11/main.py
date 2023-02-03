import random

parosszam:str = None
parosszamMasolat:str = None
paratlanszam:str=None
paratlanszamMasolat:str=None
atlag:float=0
dbatlag:int=0
darab:int=0
randszam:float=0
kozep:float=None

while (parosszam == None or  parosszam % 2 != 0):
    print("Kérek egy páros számot:", end='')
    parosszam = input()
    parosszamMasolat = parosszam.replace(".", "").replace("-", "")
    if(parosszamMasolat.isnumeric()):
        parosszam = int(parosszam)
    else:
        parosszam = None

while (paratlanszam == None or paratlanszam % 2 ==0 or parosszam> paratlanszam):
    print("Kérek egy páratlan számot:", end='')
    paratlanszam = input()
    paratlanszamMasolat = paratlanszam.replace(".", "").replace("-", "")
    if(paratlanszamMasolat.isnumeric()):
        paratlanszam = int(paratlanszam)
    else:
        paratlanszam= None

randszam = random.randrange(parosszam, paratlanszam)

kozep= ((paratlanszam-parosszam)/2) + parosszam

if(randszam < kozep):
    print(f"A {randszam} random szám a páratlan számtól van messzebb ")
else:
    print(f"A {randszam} random szám a páros számtól van messzebb")

for i in range (parosszam, paratlanszam, 1):
    atlag = atlag+ i
    dbatlag +=1
    if(i % 4 == 0):
        darab += 1

atlag = atlag/dbatlag
print(f"A két szám közti számok átlaga: {atlag}\nA 4-el osztható számok darabszáma: {darab} db")