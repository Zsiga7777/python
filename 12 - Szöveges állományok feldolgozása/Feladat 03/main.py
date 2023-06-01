from kibe import *
from roplabdas import *
from functions import *

# Írjuk ki a képernyőre az össz adatot
roplabdasok:List[Roplabdas]=fajlOlvasas()
for roplabdas in roplabdasok:
    print(roplabdas)
# - Keressük ki az ütő játékosokat az utok.txt állömányba
utok:List[Roplabdas] = posztKereses(roplabdasok, "ütő")
fajlKiiras(utok, "utok.txt" )
# - Rendezzük a játékosokat magasság szerint növekvő sorrendbe és a magaslatok.txt állományba mentsük el.
magassagKereses(roplabdasok)
fajlKiiras(roplabdasok,"magaslatok.txt")
# - Mutassuk be a nemzetisegek.txt állományba, hogy mely nemzetiségek képviseltetik magukat a röplabdavilágban mint játékosok és milyen számban.

# - atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.
# - Egy szöveges állományba, „alacsonyak.txt” keresse ki a játékosok átlagmagasságától alacsonyabb játékosokat. Az állomány tartalmazza a játékosok nevét,  magasságát és hogy mennyivel alacsonyabbak az átlagnál, 2 tizedes pontossággal.
