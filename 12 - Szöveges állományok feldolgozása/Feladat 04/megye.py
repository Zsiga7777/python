class Megye:
    def __init__(self):
        super().__init__()
        self.terulet:float=0
        self.nev:str=None

    def __str__(self) -> str:
        return f"Megye neve:{self.nev}, megye területe:{self.terulet}"