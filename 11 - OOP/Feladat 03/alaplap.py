class Alaplap:
    def __init__(self, gyarto:str, modell:str, memoriaTipusa:str, foglalat:str, maxMemoriaSebesseg:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.memoriaTipusa:str=memoriaTipusa
        self.foglalat:str=foglalat
        self.maxMemoriaSebesseg:int=maxMemoriaSebesseg
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\nmemória Típusa:{self.memoriaTipusa},\nfoglalat:{self.foglalat},\nmaximum memória sebesség:{self.maxMemoriaSebesseg} Mhz "