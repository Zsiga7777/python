from kibe import *
from konyv import *
from functions import *

#Írjuk ki a képernyőre az össz adatot
konyvek:List[Konyv]=konyvBeolvasas()
for konyv in konyvek:
    print(konyv)

#Keressük ki az informatika témajú könyveket és mentsük el őket az informatika.txt állömányba
infosKonyvek:List[Konyv]=temaKereses(konyvek)
fajlKiiras(infosKonyvek,"informatika.txt")

#Az 1900.txt állományba mentsük el azokat a könyveket amelyek az 1900-as években íródtak
#Rendezzük az adatokat a könyvek oldalainak száma szerint csökkenő sorrendbe és a sorbarakott.txt állományba mentsük el.
# „kategoriak.txt” állományba mentse el a könyveket téma szerint. Például:
# Thriller:
# 	- könnyv1
# 	- könnyv2
# Krimi:
# 	- könnyv1
# 	- könnyv2
