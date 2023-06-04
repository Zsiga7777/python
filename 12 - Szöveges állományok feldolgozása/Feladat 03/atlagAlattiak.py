class AtlgaAlattiak:
    def __init__(self):
        super().__init__()
        self.nev:str=None
        self.kulonbseg:float=0
        self.magassag:float=0
    def __str__(self) -> str:
        return f"Neve:{self.nev}, magassága:{self.magassag}cm és az átlaghoz mért különbség: {self.kulonbseg: 1.2f} cm"