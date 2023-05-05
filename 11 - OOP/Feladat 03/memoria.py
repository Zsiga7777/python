class Memoria:
    def __init__(self, gyarto:str, modell:str, memoriaTipusa:str, meret:int, maxMemoriaSebesseg:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.memoriaTipusa:str=memoriaTipusa
        self.meret:str=meret
        self.maxMemoriaSebesseg:int=maxMemoriaSebesseg
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\nmemória Típusa:{self.memoriaTipusa},\nmemória mérete:{self.meret} GB,\nmaximum memória sebesség:{self.maxMemoriaSebesseg} Mhz "
