from os import system

ellenalas1:int=None
ellenalas2:int=None
kotes:str=None
eredo:float=None

print("Kérem az egyik ellenálás értékét:",end='')
ellenalas1=int(input())
print("Kérem a másik ellenálás értékét:",end='')
ellenalas2=int(input())
print("Kérem a kötés típusát(s vagy p):",end='')
kotes=str(input())

system('cls')

match kotes:
    case "p"|"P":
        eredo=(ellenalas1 * ellenalas2) / (ellenalas1 + ellenalas2)
        print(f"{eredo}")
    case "s"|"S":
        eredo=ellenalas1+ellenalas2
        print(f"{eredo}")
    case _:
        print("Nincs ilyen kötés típus")