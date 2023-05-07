class Kerek:
    def __init__(self, gyarto:str, szelesseg:int, atmero:int, suly:int, fajta:str):
        super().__init__()
        self.gyarto:str=gyarto
        self.szelesseg:int=szelesseg
        self.atmero:int = atmero
        self.suly:int=suly
        self.fajta:str= fajta
    def __str__(self) -> str:
        return f"Gyártó:{self.gyarto}\nSzélessége:{self.szelesseg} mm\nÁtmérője:{self.atmero} inch\nSúlya:{self.suly} kg\nFajtája:{self.fajta}\n"