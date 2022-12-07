from os import system

ital:str=None

print("1-Coca Cola \n 2-Pepsi \n 3-Fanta \n 4-Spite")
print("Kérem az egyik ital számát:",end='')
ital=str(input().strip())

system('cls')

match ital:
    case "1":
        print("Ön a Coca Cola-t választotta")
    case "2":
        print("Ön a Pepsi-t választotta")
    case "3":
        print("Ön a Fanta-t választotta")
    case "4":
        print("Ön a Sprite-ot választotta")
    case _:
        print("Nincs ilyen ital")