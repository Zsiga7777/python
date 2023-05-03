class Alaplap:
    def __init__(self, gyarto:str="Asus", modell:str="ROG STRIX Z790-E GAMING WIFI", memoriaTipusa:str="DDR5", foglalat:str="LGA-1700", maxMemoriaSebesseg:int=7800):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.memoriaTipusa:str=memoriaTipusa
        self.foglalat:str=foglalat
        self.maxMemoriaSebesseg:int=maxMemoriaSebesseg
    def __str__(self) -> str:
        return f"gyarto:{self.gyarto}, modell:{self.modell}, memória Típusa:{self.memoriaTipusa}, foglalat:{self.foglalat}, maximum memória sebesség:{self.maxMemoriaSebesseg} Mhz "

class Memoria:
    def __init__(self, gyarto:str="Kingston", modell:str="FURY Renegade", memoriaTipusa:str="DDR4", meret:int=16, maxMemoriaSebesseg:int=3600):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.memoriaTipusa:str=memoriaTipusa
        self.meret:str=meret
        self.maxMemoriaSebesseg:int=maxMemoriaSebesseg
    def __str__(self) -> str:
        return f"gyarto:{self.gyarto}, modell:{self.modell}, memória Típusa:{self.memoriaTipusa}, memória mérete:{self.meret} GB, maximum memória sebesség:{self.maxMemoriaSebesseg} Mhz "

class Processzor:
    def __init__(self, gyarto:str="Intel", modell:str="i9-13900K", magokSzama:int=24, foglalat:str="LGA1700", maxOrajel:float=5.80):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.magokSzama:int=magokSzama
        self.foglalat:str=foglalat
        self.maxOrajel:float=maxOrajel
    def __str__(self) -> str:
        return f"gyarto:{self.gyarto}, modell:{self.modell}, magok száma:{self.magokSzama} DB, foglalat típusa:{self.foglalat}, maximum órajel:{self.maxOrajel} Ghz "

class Videokartya:
    def __init__(self, gyarto:str="gigabyte", modell:str="GeForce RTX™ 4090 GAMING OC 24G (rev. 1.0 / 1.1)", magokSzama:int=16384, memoriaTipus:str="GDDR6X", maxOrajel:int=2535, vram:int=24, hossz:float=340):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.magokSzama:int=magokSzama
        self.memoriaTipus:str=memoriaTipus
        self.maxOrajel:int=maxOrajel
        self.vram:int=vram
        self.hossz:float=hossz
    def __str__(self) -> str:
        return f"gyarto:{self.gyarto}, modell:{self.modell}, magok száma:{self.magokSzama} DB, memória típusa:{self.memoriaTipus}, maximum órajel:{self.maxOrajel} Ghz, memória mérete:{self.vram} GB, hossza:{self.hossz} mm "

class Hattertar:
    def __init__(self, gyarto:str="Kingston",tipus:str="M.2", modell:str="NV2 2TB M.2 (SNV2S/2000G)", tarhely:int=2, irasiSebesseg:int=2800, olvasasiSebesseg:int=3500):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.tipus:str=tipus
        self.tarhely:int=tarhely
        self.irasiSebesseg:int=irasiSebesseg
        self.olvasasiSebesseg:int=olvasasiSebesseg
    def __str__(self) -> str:
        return f"gyarto:{self.gyarto}, modell:{self.modell}, típusa:{self.tipus}, tárhelye:{self.tarhely} TB, írási sebesség:{self.irasiSebesseg} MB/s, olvasási sebesség:{self.olvasasiSebesseg} MB/s "

class Tapegyseg:
    def __init__(self, gyarto:str,tipus:str, modell:str, teljesitmeny:int, hatasfok:int, ):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.tipus:str=tipus
        self.teljesitmeny:int=teljesitmeny
        self.hatasfok:int=hatasfok

class szamitogep:
    def __init__(self, alaplap:Alaplap, processzor:Processzor, videoKartya:Videokartya, hattertar:Hattertar, memoria:Memoria, tapegyseg:Tapegyseg):
        super().__init__()
        self.alaplap:Alaplap = alaplap
        self.processzor:Processzor=processzor
        self.videoKartya:Videokartya=videoKartya
        self.hattertar:Hattertar=hattertar
        self.memoria:Memoria=memoria
        self.tapegyseg:Tapegyseg= tapegyseg