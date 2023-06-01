class Nemzetiseg:
    def __init__(self):
        super().__init__()
        self.nemzetiseg:str=None
        self.darabszam:int=0
    def __str__(self) -> str:
        return f"nemzetiség:{self.nemzetiseg}, darabszáma:{self.darabszam}"