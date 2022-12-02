from os import system

ital:int=None

print("Kérem az egyik ital számát:",end='')
ital=int(input().strip())

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