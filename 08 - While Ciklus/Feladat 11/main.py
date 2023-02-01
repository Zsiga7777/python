import random

parosszam:str = None
parosszamMasolat:str = None
paratlanszam:str=None
paratlanszamMasolat:str=None
atlag:float=0
dbatlag:int=0
darab:int=None
randszam:float=0
kozep:float=None

while (parosszam == None or parosszam == None or parosszam % 2 != 0 or paratlanszam % 2 ==0 or parosszam> paratlanszam):
    print("Kérek egy páros számot:", end='')
    parosszam = input()
    parosszamMasolat = parosszam.replace(".", "").replace("-", "")
    if(parosszamMasolat.isnumeric()):
        parosszam = int(parosszam)
    else:
        parosszam = None

    print("Kérek egy páratlan számot:", end='')
    paratlanszam = input()
    paratlanszamMasolat = paratlanszam.replace(".", "").replace("-", "")
    if(paratlanszamMasolat.isnumeric()):
        paratlanszam = int(paratlanszam)
    else:
        paratlanszam= None

randszam = random.randrange(parosszam, paratlanszam)

print(randszam)
kozep= ((paratlanszam-parosszam)/2) + parosszam

if(randszam < kozep):
    print("A random szám a páros számhoz van közelebb")
else:
    print("A páratlan számhoz van közelebb")

for i in range (parosszam, paratlanszam, 1):
    atlag = atlag+ i
    dbatlag +=1
    if(i % 4 == 0):
        darab =+1

atlag = atlag/dbatlag
print(f"A két szám közti számok átlaga: {atlag}\nA 4-el osztható számok darabszáma: {darab} db")