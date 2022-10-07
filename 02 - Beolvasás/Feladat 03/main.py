from os import system

name:str=None
height:float=None

print("Kérem a nevét:")
name=str(input())
print("Kérem a magasságát:")
height=float(input())

system('cls')

print(F"{name}, az ön magassága {height} méter.")