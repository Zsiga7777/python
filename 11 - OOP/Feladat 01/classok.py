class Negyzet:
    def __init__(self, a: float = 0):
        super().__init__()
        self.oldal: float = a

    def terulet(self) -> float:
        return self.oldal * self.oldal

    def kerulet(self) -> float:
        return 4 * self.oldal


class Telefon:
    def __init__(self):
        super().__init__()
        self.gyarto: str = "Huawei"
        self.modell: str = "Mate 20 lite"
        self.megjelenes: int = 2018
        self.akkumulator: int = 3750
        self.kijelzo: str = "IPS LCD"
        self.kijelzoMeret: float = 6.3
        self.processzor: str = "Kirin 710"
        self.memoria: int = 4
        self.tarhely: int = 64
    def kiiras(self,)->None:
        print(f"Gyarto:{self.gyarto}\nModell:{self.modell}\nMegjelenes:{self.megjelenes}\nAkkumulátor:{self.akkumulator} mAh\nKijelző:{self.kijelzo}\nKijelző Mérete:{self.kijelzoMeret} inch\nProcesszor:{self.processzor}\nMemória mérete:{self.memoria} GB\nTárhely mérete:{self.tarhely} GB")


