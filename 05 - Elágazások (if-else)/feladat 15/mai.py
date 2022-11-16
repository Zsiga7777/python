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
valasztottMenu:str=None

print("Előétel:\nZöldségleves, Húsleves, Gyümölcsleves")
print("Kérek egy kiválasztott előételt:",end='')
eloetel=int(input())

if (eloetel == 1):
    zoldsegleves= True
elif (eloetel == 2):
    husleves= True
elif (eloetel == 3):
    gyumolcsleves= True
else:
    print("Ilyen nincs")

print("Főétel:\nSültcsirkecomb, Sült csirkemell, Rakottzöldség, Spagetti, Pizza")
print("Kérek egy kiválasztott főételt:",end='')
foetel=int(input())

if (foetel == 1):
    sultcsirkecomb= True
elif (foetel == 2):
    sultCsikemell= True
elif (foetel == 3):
    rakottZoldseg= True
elif (foetel == 4):
    spagetti= True
elif (foetel == 5):
    pizza= True
else:
    print("Ilyen nincs")

print("Köret:\nRizs, Pároltzöldség, Gyümölcs, Sültkrumpli, Saláta, Kóla")
print("Kérek egy kiválasztott köretet:",end='')
koret=int(input())

if (koret == 1):
    rizs= True
elif (koret == 2):
    paroltzoldseg= True
elif (koret == 3):
    gyumolcs= True
elif (koret == 4):
    sultkrumpli= True
elif (koret == 5):
    salata= True
elif (koret == 6):
    kola= True
else:
    print("Ilyen nincs")


if((eloetel >0 and eloetel <4) and (foetel >0 and foetel <6) and (koret >0 and koret<7)):
    if()