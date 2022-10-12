from operator import le
from os import system
from turtle import st

band:str=None
songName:str=None
length:float=None

print("Kérem a banda nevét:", end="")
band=str(input())

print("Kérem a kedvenc zeneszámát:", end="")
songName=str(input())

print("Kérem a szám hosszát:", end="")
length=float(input())

system('cls')

print(F"Az ön kedvenc eggyütesének {band} a legjobb zeneszáma a {songName}, melynek hossza {length} perc. \n")