eletkor:str = None
eletkorMasolat:str = None
szam_e:bool = False

while (eletkor == None or (eletkor<0 or eletkor > 99)):
    print ("Kérem az életkorát: ", end='')
    eletkor = input()
    eletkorMasolat = eletkor.replace(".", "").replace("-","")
    szam_e = eletkorMasolat.isnumeric()
    if(szam_e):
        eletkor=float(eletkor)

if(eletkor > 0 and eletkor <= 6):
    print("Ön a gyerek korosztályba esik")
elif(eletkor > 6 and eletkor <= 18):
    print("Ön a iskolás korosztályba esik")
elif(eletkor > 18 and eletkor <= 65):
    print("Ön a dolgozó korosztályba esik")
elif(eletkor > 65 and eletkor <= 99):
    print("Ön a nyugdíjas korosztályba esik")
else:
    print("Nem esik egyik korosztályba sem")