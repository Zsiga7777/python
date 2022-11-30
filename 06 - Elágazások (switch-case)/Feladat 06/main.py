from os import system
import math

egyikOldal:int=None
masikOldal:int=None
tulajdonsag:str=None
eredmeny:float=None

print("Kérem az egyik oldal hosszát:",end='')
egyikOldal=int(input())
print("Kérem a másik oldal hosszát:",end='')
ellenalas2=int(input())
print("Kérem a kívánt tulajdonságot(t, a, k):",end='')
kotes=str(input())

system('cls')

match kotes:
    case "t":
        eredmeny=egyikOldal * masikOldal
        print(f"{eredmeny} cm2")
    case "k":
        eredmeny=2*(egyikOldal+masikOldal)
        print(f"{eredmeny} cm")
    case "a":
        eredmeny=math.sqrt((egyikOldal**2 + masikOldal**2))
        print(f"{eredmeny}")
    case _:print("Valami nem stimmel")