from os import system

ellenalas1:int=None
ellenalas2:int=None
kotes:str=None
eredo:float=None

print("Kérem az egyik ellenálás értékét:",end='')
ellenalas1=int(input().strip())
print("Kérem a másik ellenálás értékét:",end='')
ellenalas2=int(input().strip())
print("Kérem a kötés típusát(s vagy p):",end='')
kotes=str(input()).strip().lower()

system('cls')

match kotes:
    case "p":
        eredo=(ellenalas1 * ellenalas2) / (ellenalas1 + ellenalas2)
        print(f"{eredo}")
    case "s":
        eredo=ellenalas1+ellenalas2
        print(f"{eredo}")
    case _:
        print("Nincs ilyen kötés típus")