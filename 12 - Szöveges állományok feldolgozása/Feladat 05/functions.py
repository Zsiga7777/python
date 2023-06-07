from film import *
from typing import *

def osszBevetel(filmek:List[Film])->float:
    osszes:float=0
    for film in filmek:
        osszes += film.bevetel
    return osszes

def legnagyobbErtekeles(filmek:List[Film])->Film:
    legjobbFilm:Film=Film()
    for film in filmek:
        if(film.nezoiErtekeles > legjobbFilm.nezoiErtekeles):
            legjobbFilm=film
    return legjobbFilm

def rottenTomatoesxSzazalekFolott(filmek:List[Film])->bool:
    vanE:bool=False
    for film in filmek:
        if(film.rottenTomatoes >=90):
            vanE = True
            return vanE