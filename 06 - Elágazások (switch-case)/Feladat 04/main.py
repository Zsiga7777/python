from os import system

szam1:int=None
szam2:int=None
muveletiJel:str=None
osszeg:float=None

print("Kérek  egy számot:",end='')
szam1=int(input())
print("Kérek  egy másik számot:",end='')
szam2=int(input())
print("Kérek egy műveleti jelet:",end='')
muveletiJel=str(input())

system('cls')

match muveletiJel:
    case "+":
        osszeg=szam1+szam2
        print(f"{osszeg}")
    case "-":
        osszeg=szam1-szam2
        print(f"{osszeg}")
    case "*":
        osszeg=szam1*szam2
        print(f"{osszeg}")
    case "/":
        osszeg=szam1/szam2
        print(f"{osszeg}")
    case _:
        print("Nincs ilyen műveleti jel")