from os import system

uditoSzama:str=None
uditoSzamaMasolat:str=None
szam_e:bool=False

while(uditoSzama == None or szam_e == False or uditoSzama < 0 or uditoSzama >6):
    system('cls')
    print("Az üditő kínálat:\n1: Fanta\n2: Kóla\n3: iceTea\n4: Pepsi\n5: víz")
    print("Kérem az ön által választott italt:",end='')
    uditoSzama=input()
    uditoSzamaMasolat = uditoSzama.replace(".", "").replace("-","")
    szam_e =uditoSzamaMasolat.isnumeric()
    if(szam_e):
        uditoSzama = int(uditoSzama)

match uditoSzama:
    case 1:
        print("Fantát választott")
    case 2:
        print("Kólát választott")
    case 3:
        print("iceTea-t választott")
    case 4:
        print("Pepsi-t választott")
    case 5:
        print("vizet választott")
    case _:
        print("Nem megfelő számot adott meg.")

