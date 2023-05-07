class Zsebkendo:
    def __init__(self, alapanyag:str, hossz:float, szelesseg:float, retegSzam:int, gyarto:str):
        super().__init__
        self.alapanyag:str=alapanyag
        self.hossz:float=hossz
        self.szelesseg:float=szelesseg
        self.retegSzam:int=retegSzam
        self.gyarto:str=gyarto
    def __str__(self) -> str:
        return f"Gyártója:{self.gyarto},\nRétegek száma:{self.retegSzam} DB,\nAlapanyaga:{self.alapanyag},\nHossza:{self.hossz} cm,\nSzélessége:{self.szelesseg} cm\n"