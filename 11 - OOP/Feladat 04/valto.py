class Valto:
    def __init__(self, gyarto:str, fokozatokSzama:int, mod:str, tipus:str):
        super().__init__()
        self.gyarto:str=gyarto
        self.fokozatokSzama:int=fokozatokSzama
        self.mod:str = mod
        self.tipus:str=tipus
    def __str__(self) -> str:
        return f"Gyártó:{self.gyarto}\nFokozatok száma:{self.fokozatokSzama} Db\nTípusa:{self.tipus}\nModja:{self.mod}\n"