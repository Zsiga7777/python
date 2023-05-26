class Kezilabdas:
    def __init__(self):
        super().__init__()
        self.nev:str=None
        self.magassag:int=0
        self.poszt:str=None
        self.nemzetiseg:str=None
        self.csapat:str=None
        self.orszag:str=None
    def __str__(self) -> str:
        return f"Név:{self.nev}, magasság:{self.magassag} cm, poszt:{self.poszt}, nemzetiség:{self.nemzetiseg}, csapat:{self.csapat}, ország:{self.orszag}"