class Hattertar:
    def __init__(self, gyarto:str,tipus:str, modell:str, tarhely:int, irasiSebesseg:int, olvasasiSebesseg:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.modell:str=modell
        self.tipus:str=tipus
        self.tarhely:int=tarhely
        self.irasiSebesseg:int=irasiSebesseg
        self.olvasasiSebesseg:int=olvasasiSebesseg
    def __str__(self) -> str:
        return f"gyartó:{self.gyarto},\nmodell:{self.modell},\ntípusa:{self.tipus},\ntárhelye:{self.tarhely} TB,\nírási sebesség:{self.irasiSebesseg} MB/s,\nolvasási sebesség:{self.olvasasiSebesseg} MB/s "
