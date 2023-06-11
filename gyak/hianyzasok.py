def megrovas(hianyzasokSzama:int)->str:
    eredmeny:str=None
    if(hianyzasokSzama <=4 and hianyzasokSzama >=1):
        eredmeny="figyelmeztetés"
    elif(hianyzasokSzama <=10 and hianyzasokSzama >=5):
        eredmeny="osztályfőnöki megrovás"
    elif(hianyzasokSzama <=30 and hianyzasokSzama >=11):
        eredmeny="igazgatói megrovás"
    elif(hianyzasokSzama > 30 ):
        eredmeny="elbocsájtás az iskolából"
    else   :
        eredmeny="nem értelmezhető"
    return eredmeny

while True:
    print("Adja meg a tanuló nevét: ", end='')
    diakNeve:str=input()
    if(diakNeve==""):
        break

    print("Adja meg a tanuló igazolatlan hiányzásainak számát:", end='')
    hianyzasokSzama:int=int(input())

    eredmeny:str=megrovas(hianyzasokSzama)
    print(f"{diakNeve}: {eredmeny}")