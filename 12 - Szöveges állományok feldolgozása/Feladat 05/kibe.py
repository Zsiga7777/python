from film import *
from typing import *
import os
def fajlbeolvasas()->List[Film]:
    alaput:str=os.path.pardir(os.path.abspath(__file__))
    alaput += "/data/filmek.csv"
    egysor:str=None
    adat:List=[]
    film:Film=None
    filmek:List[Film]=[]
    try:
        with open (alaput,mode="r",encoding="utf-8") as file:
            for sor in file:
                egysor=sor.strip()
                adat=egysor.split(",")
                film.film=adat[0]
                film.mufaj=adat[1]
                film.forgalmazo=adat[2]
                film.nezoiErtekeles=int(adat[3])
                film.megterules=float(adat[4])
                film.rottenTomatoes=int(adat[5])
                film.bevetel=float(adat[6])
                film.megjelenes=int(adat[7])
                filmek.append(film)
            return filmek
    except FileNotFoundError as ex:
        print(f"valami nyűg van a fájlal {ex.filename}")
        return []