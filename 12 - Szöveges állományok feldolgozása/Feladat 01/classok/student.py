class Student:
    def __init__(self):
        super().__init__()
        self.nev:str= None
        self.atlag:float=0
    
    def __str__(self) -> str:
        return f"{self.nev} : {self.atlag}"