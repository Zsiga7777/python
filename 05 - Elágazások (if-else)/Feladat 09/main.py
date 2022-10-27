from os import system

x:int=None
y:int=None

print("Kérek egy számot:",end='')
x=int(input())

print("Kérek egy másik számot:",end='')
y=int(input())

system('cls')

if( x%y ==0 ):
    print("A második szám osztója az elsőnek.")
else:
    print("A második szám nem osztója az elsőnek")