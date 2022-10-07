from os import system

name:str=None
birthyear:int=None

print("Kérem a nevét: ")
name=str(input())
print("Kérem a születési évét:")
birthyear=int(input())

system('cls')

print(F"{name}, ön {birthyear}-ben született! \n")

