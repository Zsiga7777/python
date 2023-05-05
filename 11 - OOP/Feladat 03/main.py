from szamitogep import *
from tapegyseg import *
from hattertar import *
from videokartya import *
from memoria import *
from processzor import *
from alaplap import *

alaplap:Alaplap=Alaplap("Asus","ROG STRIX Z790-E GAMING WIFI","DDR5","LGA-1700",7800)
memoria:Memoria=Memoria("Kingston","FURY Renegade","DDR4",16,3600)
processzor:Processzor=Processzor("Intel","i9-13900K",24,"LGA1700",5.80)
videokartya:Videokartya=Videokartya("gigabyte","GeForce RTX™ 4090 GAMING OC 24G (rev. 1.0 / 1.1)",16384,"GDDR6X",2535,24,340)
hattertar:Hattertar=Hattertar("Kingston","M.2","NV2 2TB M.2 (SNV2S/2000G)",2,2800,3500)
tapegyseg:Tapegyseg=Tapegyseg("Corsair","Moduláris","AX1600i Digital ATX Power Supply — 1600 Watt Fully-Modular PSU",1600,80)
szamitogep:Szamitogep=Szamitogep(alaplap,processzor,videokartya,hattertar,memoria,tapegyseg)

print(f"{szamitogep}")