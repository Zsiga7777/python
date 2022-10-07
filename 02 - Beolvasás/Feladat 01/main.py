from os import system

myName:str=None

print("Adja meg a nevét: ")
myName=str(input())

system('cls')

print(F"Üdvözlöm {myName}!\n")
