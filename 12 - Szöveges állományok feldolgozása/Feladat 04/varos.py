class Varos:
    def __init__(self):
        super().__init__()
        self.nev:str=None
        self.varosTipusa:str=None 
        self.megyeNeve:str=None
        self.jaras:str=None
        self.kisterseg:str=None
        self.nepesseg:int=0
        self.terulet:float=0
    def __str__(self) -> str:
        return f"Város neve:{self.nev}, város típusa:{self.varosTipusa}, megye neve:{self.megyeNeve}, járás:{self.jaras}, kistérség:{self.kisterseg}, népesség:{self.nepesseg} fő, területe:{self.terulet} km2"