from os import system

zoldsegleves:bool=False
husleves:bool=False
gyumolcsleves:bool=False

sultcsirkecomb:bool=False
sultCsikemell:bool=False
rakottZoldseg:bool=False
spagetti:bool=False
pizza:bool=False

rizs:bool=False
paroltzoldseg:bool=False
gyumolcs:bool=False
sultkrumpli:bool=False
salata:bool=False
kola:bool=False

eloetel:int=None
foetel:int=None
koret:int=None
ertekeles:str = None

leves:str=None
masodik:str=None
koretes:str=None

print("Előétel:\nZöldségleves, Húsleves, Gyümölcsleves")
print("Kérek egy kiválasztott előételt:",end='')
eloetel=int(input())

if (eloetel == 1):
    zoldsegleves= True
    leves:str="zöldség leves"
elif (eloetel == 2):
    husleves= True
    leves:str="húsleves"
elif (eloetel == 3):
    gyumolcsleves= True
    leves:str="gyümölcsleves"
else:
    print("Ilyen nincs")

print("Főétel:\nSültcsirkecomb, Sült csirkemell, Rakottzöldség, Spagetti, Pizza")
print("Kérek egy kiválasztott főételt:",end='')
foetel=int(input())

if (foetel == 1):
    sultcsirkecomb= True
    masodik:str= "sültcsirkecomb" 
elif (foetel == 2):
    sultCsikemell= True
    masodik:str= "sült csirkemell" 
elif (foetel == 3):
    rakottZoldseg= True
    masodik:str= "rakottzöldség" 
elif (foetel == 4):
    spagetti= True
    masodik:str= "spagetti" 
elif (foetel == 5):
    pizza= True
    masodik:str= "pizza" 
else:
    print("Ilyen nincs")

print("Köret:\nRizs, Pároltzöldség, Gyümölcs, Sültkrumpli, Saláta, Kóla")
print("Kérek egy kiválasztott köretet:",end='')
koret=int(input())

if (koret == 1):
    rizs= True
    koretes:str= "rizs" 
elif (koret == 2):
    paroltzoldseg= True
    koretes:str= "pároltzöldség" 
elif (koret == 3):
    gyumolcs= True
    koretes:str= "gyümölcs" 
elif (koret == 4):
    sultkrumpli= True
    koretes:str= "sültkrumpli" 
elif (koret == 5):
    salata= True
    koretes:str= "saláta" 
elif (koret == 6):
    kola= True
    koretes:str= "kóla" 
else:
    print("Ilyen nincs")


if((eloetel >0 and eloetel <4) and (foetel >0 and foetel <6) and (koret >0 and koret<7)):
    if(zoldsegleves and spagetti and (gyumolcs or salata) and pizza!=True and rakottZoldseg !=True):
        ertekeles ="Kiváló"
    elif(zoldsegleves and sultCsikemell and rizs and sultkrumpli!=True):
        ertekeles ="fitnesz menü"
    elif(husleves  and sultcsirkecomb  and salata  or sultkrumpli and rakottZoldseg != True and pizza !=True):
        ertekeles ="vasárnapi menü"
    elif (spagetti  or pizza and gyumolcs  or kola  and rakottZoldseg !=True and paroltzoldseg!=True):
        ertekeles ="napimenü"
else:
    print("nem teljes a rendelés")

if (ertekeles ==None):
    ertekeles:str= "Egyedi"

system('cls')

print(f"A választott menü értékelése:{ertekeles} \n A választott menü: {leves}, {masodik}, {koretes}")