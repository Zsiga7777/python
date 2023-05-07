class Karosszeria:
    def __init__(self, gyarto:str, suly:int, alapanyag:str, ajtokSzama:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.suly:int=suly
        self.alapanyag:str = alapanyag
        self.ajtokSzama:int=ajtokSzama
    def __str__(self) -> str:
        return f"Gyártó:{self.gyarto}\nSuly:{self.suly} kg\nAlapanyag:{self.alapanyag}\nAjtók száma:{self.ajtokSzama} Db\n"