class Almafa:
    def __init__(self, elettertam:float, termes:str, atlagosMeret:float, viragokSzine:str, ):
        super().__init__()
        self.elettartam:float=elettertam
        self.termes:str=termes
        self.atlagosMeret:float = atlagosMeret
        self.viragokSzine:str=viragokSzine
    def __str__(self) -> str:
        return f"Termése:{self.termes}\nVirágának színe:{self.viragokSzine}\nÁtlagos élettartama:{self.elettartam} év\nA fa átlagos magassága:{self.atlagosMeret} méter\n"