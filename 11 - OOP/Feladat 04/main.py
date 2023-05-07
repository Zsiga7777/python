from almafa import *
from zsebkendo import *
from motor import Motor
from valto import *
from karosszeria import *
from kerek import *
from auto import Auto

fa:Almafa=Almafa(50,"alma",15,"fehér")
print(f"{fa}")

zsebkendo:Zsebkendo=Zsebkendo("papír",21,20,3,"Zewa")
print(f"{zsebkendo}")

motor:Motor=Motor("Opel",1998,4,170,200,True)
valto:Valto=Valto("Opel",6,"Autómata","Tolókerekes")
karosszeria:Karosszeria=Karosszeria("Opel",750,"alumínium",5)
kerek:Kerek=Kerek("Opel",225,17,10,"nyári")
auto:Auto=Auto(motor,valto,karosszeria,kerek)
print(f"{auto}")