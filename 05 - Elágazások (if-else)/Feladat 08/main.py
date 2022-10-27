from os import system

szam:int=None
eredmenyElso:int=None
eredmenyMasodik:int=None

print("Kérek egy számot:",end='')
szam=int(input())

eredmenyElso=szam%4
eredmenyMasodik=szam%6

system('cls')

if ( eredmenyElso == 0 and eredmenyMasodik == 0 ):
    print("A szám osztható 4-el és 6-al")
elif ( eredmenyElso == 0 and eredmenyMasodik !=0 ):
    print("A szám csak 4-el osztható")
elif ( eredmenyElso != 0 and eredmenyMasodik ==0 ):
    print("A szám csak 6-el osztható")
else:
    print("A szám nem osztható sem 6-al, sem 4-el.")
