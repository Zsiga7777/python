from os import system

ital:str=None

print("Kérek az egyik ital számát:",end='')
ital=str(input())

system('cls')

match ital:
    case "1":
        print("Ön a Coca Cola-t választotta")
    case "2":
        print("Ön a Pepsi-t választotta")
    case "3":
        print("Ön a Fantá-t választotta")
    case "4":
        print("Ön a Sprite-ot választotta")
    case _:
        print("Nincs ilyen ital")