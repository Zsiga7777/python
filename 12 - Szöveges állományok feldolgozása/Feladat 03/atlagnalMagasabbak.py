class Atlagfelettiek:
    def __init__(self):
        super().__init__()
        self.nev:str=None
        self.magassag:float=0
    def __str__(self) -> str:
        return f"{self.nev} {self.magassag}cm magas"