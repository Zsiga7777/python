import random

randszam :int =random(0,9)
tip:int=None
elet:int=5

print("Kérek egy számot:", end='')
tip = int(input)

while (randszam != tip and elet > 0):
    elet -= 1
    print(f"Kérek egy számot: \ még {elet}-e van", end='')
    tip = int(input)

print(f"Gratulálok! A helyes szám a {randszam} volt.")
