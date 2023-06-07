from film import *
from typing import *
import os
def fajlbeolvasas()->List[Film]:
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    alaput += "/data/filmek.csv"
    egysor:str=None
    adat:List=[]
    film:Film=None
    filmek:List[Film]=[]
    try:
        with open (alaput,mode="r",encoding="utf-8") as file:
            for sor in file:
                film=Film()
                egysor=sor.strip()
                adat=egysor.split(",")
                film.film=adat[0]
                film.mufaj=adat[1]
                film.forgalmazo=adat[2]
                film.nezoiErtekeles=int(adat[3])
                film.megterules=float(adat[4])
                film.rottenTomatoes=int(adat[5])
                film.bevetel=float(adat[6].replace("$",""))
                film.megjelenes=int(adat[7])
                filmek.append(film)
            return filmek
    except FileNotFoundError as ex:
        print(f"valami nyűg van a fájlal {ex.filename}")
        return []
    
def kiiras(filmek:List[Film],fajlnev:str)->None:
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    alaput+="/output/"
    teljesut:str=os.path.join(alaput,fajlnev)
    try:
        with open(teljesut,mode="w",encoding="utf-8") as file:
            for film in filmek:
                file.write(f"film")
        print("Sikerült")
    except FileNotFoundError as er:
        print(f"Valami nem sikerült a {er.filename}")
    