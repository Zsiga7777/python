class Motor:
    def __init__(self, gyarto:str, hengerUrtartalom:int, hengerekSzama:int, loero:int, nyomatek:int, turbo:bool ):
        super().__init__()
        self.gyarto:str=gyarto
        self.hengerUrtartalom:int=hengerUrtartalom
        self.hengerekSzama:int = hengerekSzama
        self.loero:int=loero
        self.nyomatek:int=nyomatek
        self.turbo:bool=turbo
    def __str__(self) -> str:
        return f"Gyártó:{self.gyarto}\nHengerűrtartalom:{self.hengerUrtartalom} cm3\nHengerek száma:{self.hengerekSzama} Db\nTeljesítmény:{self.loero} lóerő\nNyomaték:{self.nyomatek} NM\nTurbó van-e:{self.turbo}\n"