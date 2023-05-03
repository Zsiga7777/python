class Alaplap:
    def __init__(self, gyarto:str="Asus", modell:str="ROG STRIX Z790-E GAMING WIFI", memoriaTipusa:str="DDR5", foglalat:str="LGA-1700", maxMemoriaSebesseg:int=7800):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.memoriaTipusa:str=memoriaTipusa
        self.foglalat:str=foglalat
        self.maxMemoriaSebesseg:int=maxMemoriaSebesseg
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\nmemória Típusa:{self.memoriaTipusa},\nfoglalat:{self.foglalat},\nmaximum memória sebesség:{self.maxMemoriaSebesseg} Mhz "

class Memoria:
    def __init__(self, gyarto:str="Kingston", modell:str="FURY Renegade", memoriaTipusa:str="DDR4", meret:int=16, maxMemoriaSebesseg:int=3600):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.memoriaTipusa:str=memoriaTipusa
        self.meret:str=meret
        self.maxMemoriaSebesseg:int=maxMemoriaSebesseg
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\nmemória Típusa:{self.memoriaTipusa},\nmemória mérete:{self.meret} GB,\nmaximum memória sebesség:{self.maxMemoriaSebesseg} Mhz "

class Processzor:
    def __init__(self, gyarto:str="Intel", modell:str="i9-13900K", magokSzama:int=24, foglalat:str="LGA1700", maxOrajel:float=5.80):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.magokSzama:int=magokSzama
        self.foglalat:str=foglalat
        self.maxOrajel:float=maxOrajel
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\nmagok száma:{self.magokSzama} DB,\nfoglalat típusa:{self.foglalat},\nmaximum órajel:{self.maxOrajel} Ghz "

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
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\nmagok száma:{self.magokSzama} DB,\nmemória típusa:{self.memoriaTipus},\nmaximum órajel:{self.maxOrajel} Mhz,\nmemória mérete:{self.vram} GB,\nhossza:{self.hossz} mm "

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
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\ntípusa:{self.tipus},\ntárhelye:{self.tarhely} TB,\nírási sebesség:{self.irasiSebesseg} MB/s,\nolvasási sebesség:{self.olvasasiSebesseg} MB/s "

class Tapegyseg:
    def __init__(self, gyarto:str="Corsair",tipus:str="Moduláris", modell:str="AX1600i Digital ATX Power Supply — 1600 Watt Fully-Modular PSU", teljesitmeny:int=1600, hatasfok:int=80, ):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.tipus:str=tipus
        self.teljesitmeny:int=teljesitmeny
        self.hatasfok:int=hatasfok
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\ntípusa:{self.tipus},\nteljesítménye:{self.teljesitmeny} W,\nhatásfoka:{self.hatasfok} %"

class Szamitogep:
    def __init__(self, alaplap:Alaplap=Alaplap(), processzor:Processzor=Processzor(), videoKartya:Videokartya=Videokartya(), hattertar:Hattertar=Hattertar(), memoria:Memoria=Memoria(), tapegyseg:Tapegyseg=Tapegyseg()):
        super().__init__()
        self.alaplap:Alaplap = alaplap
        self.processzor:Processzor=processzor
        self.videoKartya:Videokartya=videoKartya
        self.hattertar:Hattertar=hattertar
        self.memoria:Memoria=memoria
        self.tapegyseg:Tapegyseg= tapegyseg
    def __str__(self) -> str:
        return f"alaplap:{self.alaplap}\n\nprocesszor:{self.processzor}\n\nvideókártya:{self.videoKartya}\n\nháttértár:{self.hattertar}\n\nmemória:{self.memoria}\n\ntápegység:{self.tapegyseg}"