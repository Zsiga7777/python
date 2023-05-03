class Negyzet:
    def __init__(self, a: float = 0):
        super().__init__()
        self.oldal: float = a

    def terulet(self) -> float:
        return self.oldal * self.oldal

    def kerulet(self) -> float:
        return 4 * self.oldal


class Telefon:
    def __init__(self, gyarto:str="Huawei" , modell:str = "Mate 20 lite", megjelenes:int= 2018, akkumulator:int= 3750, kijelzo:str= "IPS LCD", kijelzoMeret:float= 6.3, processzor:str="Kirin 710", memoria:int= 4, tarhely:int=64):
        super().__init__()
        self.gyarto: str = gyarto
        self.modell: str = modell
        self.megjelenes: int = megjelenes
        self.akkumulator: int = akkumulator
        self.kijelzo: str = kijelzo
        self.kijelzoMeret: float = kijelzoMeret
        self.processzor: str = processzor
        self.memoria: int = memoria
        self.tarhely: int = tarhely

    def kiiras(self)->None:
        print(f"Gyarto:{self.gyarto}\nModell:{self.modell}\nMegjelenes:{self.megjelenes}\nAkkumulátor:{self.akkumulator} mAh\nKijelző:{self.kijelzo}\nKijelző Mérete:{self.kijelzoMeret} inch\nProcesszor:{self.processzor}\nMemória mérete:{self.memoria} GB\nTárhely mérete:{self.tarhely} GB")


