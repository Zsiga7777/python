class Tapegyseg:
    def __init__(self, gyarto:str,tipus:str, modell:str, teljesitmeny:int, hatasfok:int, ):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.tipus:str=tipus
        self.teljesitmeny:int=teljesitmeny
        self.hatasfok:int=hatasfok
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\ntípusa:{self.tipus},\nteljesítménye:{self.teljesitmeny} W,\nhatásfoka:{self.hatasfok} %"