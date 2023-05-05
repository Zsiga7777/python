class Processzor:
    def __init__(self, gyarto:str, modell:str, magokSzama:int, foglalat:str, maxOrajel:float):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.magokSzama:int=magokSzama
        self.foglalat:str=foglalat
        self.maxOrajel:float=maxOrajel
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\nmagok száma:{self.magokSzama} DB,\nfoglalat típusa:{self.foglalat},\nmaximum órajel:{self.maxOrajel} Ghz "