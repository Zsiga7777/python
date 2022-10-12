from os import system
from statistics import mode

marka:str=None
megjelenesiEv:int=None
modell:str=None
tipus:str=None
kobcenti:int=None

print("Kérem az autó márkáját: ",end='')
marka=str(input())

print("Kérem a megjelenési évét:", end='')
megjelenesiEv=int(input())

print("kérem a modell nevét: ", end='')
modell=str(input())

print("kérem a típusát: ", end='')
tipus=str(input())

print("Kérem a motor hengerűrtalmalmát: ", end='')
kobcenti=int(input())

system('cls')

print(F"Márka:{marka} \n Modell:{modell} \n Típus:{tipus} \n Köbcenti:{kobcenti} \n")