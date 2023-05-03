class Motor:
    def __init__(self, gyarto:str, tipus:str, modell:str, uzemanyagFogyasztas:float, gyartasEve:int, nyomatek:int, hengerekSzama:int, loero:int):
        super().__init__() 
        self.gyarto:str = gyarto
        self.tipus:str = tipus
        self.modell:str = modell
        self.uzemanyagFogyasztas:float = uzemanyagFogyasztas
        self.gyartasEve:int = gyartasEve
        self.nyomatek:int = nyomatek
        self.hengerekSzama:int= hengerekSzama
        self.loero:int= loero
    def __str__(self) -> str:
        return f"{self.gyarto} {self.modell} ({self.gyartasEve})"