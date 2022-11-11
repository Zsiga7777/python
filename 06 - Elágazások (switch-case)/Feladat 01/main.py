from os import system

nap:str=None

print("Kérem a hét valahanyadik napját :",end='')
nap=str(input())

system('cls')

match nap:
    case "1":
        print("hétfő")
    case "2":
        print("kedd")
    case "3":
        print("szerda")
    case "4":
        print("csütörtök")
    case "5":
        print("péntek")
    case "6":
        print("szombat")
    case "7":
        print("vasárnap")
    case _:
        print("Nincs ilyen nap")