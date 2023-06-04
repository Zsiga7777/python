from varos import *
from functions import *
from kibe import *
from megye import *

varosok:List[Varos]=fajlBeolvasas()
# - Írjuk ki a képernyőre az össz adatot
for varos in varosok:
    print(f"{varos}")
# - Keressük ki a megyeszékhely megyei jogú városokat és mentsük el a megyejoguvarosok.txt állományba
megyeszekhelyek:List[Varos]=megyeszekhelyKereses(varosok)
fajlkiiras(megyeszekhelyek, "megyejoguvarosok.txt")

# - Az nepesseg.txt állományba mentsük el azokat a településeket és a hozzájuk tartozó adatokat, ahol a népesség 50.000 és 100.000 közt van
megfeleloVarosok:List[Varos]=nepessegKereses(varosok)
fajlkiiras(megfeleloVarosok,"nepesseg.txt" )
# - Keressük ki azokat a településeket, melyek területei meghaladják az 200-at  és a  nagyteruletek.txt állományba mentsük el.
megfeleloTeruletuVarosok:List[Varos]=teruletKereses(varosok)
fajlkiiras(megfeleloTeruletuVarosok,"nagyteruletek.txt" )
# - Keressük ki Békés megye össz települését és a bekes.txt állományba mentsük el.
megfeleloMegyebeVarosok:List[Varos]=megyeKereses(varosok, "Békés")
fajlkiiras(megfeleloMegyebeVarosok,"bekes.txt")
# - megyeterületek.txt állományba mentsük el a megye nevét és területének nagyságát.
megyek:Megye=megyeTeruletSzamitas(varosok)
fajlkiiras(megyek,"megyeterületek.txt")