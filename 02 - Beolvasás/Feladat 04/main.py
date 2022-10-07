from os import system
import sys

name:str=None
lenyomottBillentyu:str=None

name=str(input("Kérem a nevét: "))
lenyomottBillentyu=str(input("Nyomjon le egy billentyűt: "))

system('cls')

print(F"{name}, ön a/az {lenyomottBillentyu}-t nyomta le!")