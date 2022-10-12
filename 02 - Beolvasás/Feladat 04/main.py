from os import system
import sys

nev:str=None
lenyomottBillentyu:str=None

print("Kérem a nevét: ", end='')
name=str(input())

print("Nyomjon le egy billentyűt: ",end='')
lenyomottBillentyu=str(input())

system('cls')

print(F"{nev}, ön a/az {lenyomottBillentyu}-t nyomta le!")