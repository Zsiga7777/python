from kibe import *
from functions import *
from film import *

# feladat – 1:
# -	Írjuk ki a képernyőre a minta szerint, hogy hány film adata szerepel az a filmek.csv állományban.
# Feladat 1:
# A filmek.csv állományban 78 film szerepel.
filmek:List[Film]=fajlbeolvasas()
filmekSzam:int=len(filmek)
print(f"A filmek.csv állományban {filmekSzam} film szerepel.")

# feladat – 2:
# -	Írjuk ki a képernyőre a minta szerint, hogy mekkora az össz bevétele a filmek.csv állományban található filmeknek.
# Feladat 2:
# A filmek.csv állományban szerepelő filmek ösz bevétele $11181.75 millió dollár.
# .
osszesen:float=osszBevetel(filmek)
print(f"A filmek.csv állományban szerepelő filmek ösz bevétele ${osszesen:1.2f} millió dollár.")

# feladat – 3:
# -	Írjuk ki a képernyőre a minta szerint, hogy a filmek.csv állományban található filmek közül melyik az a film amelyik a legnagyobb nézői értékelést kapta. Feltételezheti, hogy csak egy ilyen van!
# Feladat 3:
# A legnagyobb értékelést a  Dangerous Method című film kapta (89%).
legjobbFilm:Film=legnagyobbErtekeles(filmek)
print(f"A legnagyobb értékelést a  {legjobbFilm.film} című film kapta ({legjobbFilm.nezoiErtekeles}%).")

# feladat – 4:
# -	Írjuk ki a képernyőre a minta szerint, hogy van-e olyan film, amely a Rotten Tomatoes értékelése alapján legalább 90% értékelést kapott.
# Feladat 4:
# Van / Nincs olyan film, amely a Rotten Tomatoes értékelése alapján legalább 90% értékelést kapott.
van:bool=rottenTomatoesxSzazalekFolott(filmek)
if(van== True):
    print("Van olyan film, amely a Rotten Tomatoes értékelése alapján legalább 90% értékelést kapott.")
else:
    print("Nincs olyan film, amely a Rotten Tomatoes értékelése alapján legalább 90% értékelést kapott.")
# feladat – 6:
# -	Az evek.txt állományban mentsük el a minta szerint a filmeket címeit megjelenési évre csoportositva. A megjelenési éveket rendezze növekvő sorrendbe. A konzolra írja ki, hogy a feladat mentése sikeres volt-e vagy nem.
# Feladat 6:
# A mentés sikeres volt / nem volt sikeres.

