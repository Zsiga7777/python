from typing import *
from student import *
from studentIO import *
from functions import *
from kibe import *

students:List[Student] = tanuloBekeres()

#     1 - Írjuk ki minden diák adatát a képernyőre!
for student in students:
    print(student)
# 2 - Hány diák jár az osztályba?
osztalyLetszam:int=len(students)
print(f"\n\nAz osztály létszáma:{osztalyLetszam}\n\n")
# 3 - Mennyi az osztály átlaga?
atlag:float=atlagSztamitas(students)
print(f"\n\nAz osztály átlaga:{atlag:1.2f}\n\n")
# 4 - Keressük a legtöbb pontot elért érettségizőt és írjuk ki az adatait a képernyőre.
legjobbTanulo:Student=legnyagobbSzamitas(students)
print(f"\n\nA legjobb tamuló:{legjobbTanulo.nev}\n\n")
# 5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
atlafFeletteiT :List[Student]=atlagFeletti(students,atlag)
kiiras(atlafFeletteiT, "atlagfelett.txt")
# 6 - Van e kitünő tanulónk?
# 7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
#     Értékhatárok:
# 	- elégtelen, ha: 0.00 - 1.99
# 	- elégséges, ha: 2.00 - 2.99
# 	- jó, ha: 3.00 - 3.99
# 	- jeles, ha: 4.00 - 4.99
# 	- kitünő, ha: 5.00
