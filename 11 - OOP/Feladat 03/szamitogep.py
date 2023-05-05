from tapegyseg import *
from hattertar import *
from videokartya import *
from memoria import *
from processzor import *
from alaplap import *

class Szamitogep:
    def __init__(self, alaplap:Alaplap, processzor:Processzor, videoKartya:Videokartya, hattertar:Hattertar, memoria:Memoria, tapegyseg:Tapegyseg):
        super().__init__()
        self.alaplap:Alaplap = alaplap
        self.processzor:Processzor=processzor
        self.videoKartya:Videokartya=videoKartya
        self.hattertar:Hattertar=hattertar
        self.memoria:Memoria=memoria
        self.tapegyseg:Tapegyseg= tapegyseg
    def __str__(self) -> str:
        return f"alaplap:{self.alaplap}\n\nprocesszor:{self.processzor}\n\nvideókártya:{self.videoKartya}\n\nháttértár:{self.hattertar}\n\nmemória:{self.memoria}\n\ntápegység:{self.tapegyseg}"