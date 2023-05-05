class Videokartya:
    def __init__(self, gyarto:str, modell:str, magokSzama:int, memoriaTipus:str, maxOrajel:int, vram:int, hossz:float):
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
