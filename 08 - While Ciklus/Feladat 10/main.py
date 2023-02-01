from os import system

bekertSzam:str=None
bekertSzamMasolat:str=None
osszeg:int=0
darabszam:int=-1
szam_e:bool=False

while(bekertSzam == None or szam_e == False or bekertSzam<0 or bekertSzam >99):
    print("Kérek egy egész számot:", end='')
    bekertSzam = input()
    bekertSzamMasolat = bekertSzam.replace(".", "").replace(".", "")
    szam_e = bekertSzamMasolat.isnumeric()
    if(szam_e):
        bekertSzam = int(bekertSzam)

system('cls')

print("A páros számok:")
for i in range (0, bekertSzam+1, 1):
    if(i %2 == 0):
        print(f"{i}, ", end='')
    if (i % 5 == 0):
        osszeg = osszeg + i
    if(i % 11 == 0):
        darabszam +=1
print(f"\nAz öttel osztható számok összege : {osszeg}\nA 11-el osztható számok száma:{darabszam} db.\nA héttel osztott számok, melyeknek a maradéka 3:")
for i in range(0, bekertSzam+1, 1):
    if(i % 7 == 3):
        print(f"{i}, ", end='')