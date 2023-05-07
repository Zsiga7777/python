from motor import Motor
from valto import *
from karosszeria import *
from kerek import *

class Auto:
    def __init__(self, motor:Motor, valto:Valto, karosszeria:Karosszeria, kerek:Kerek):
        super().__init__()
        self.motor:Motor=motor
        self.valto:Valto=valto
        self.karosszeria:Karosszeria = karosszeria
        self.kerek:Kerek=kerek
    def __str__(self) -> str:
        return f"Motor:\n{self.motor}\nVáltó:\n{self.valto}\nKarosszéria:\n{self.karosszeria}\nKerék:\n{self.kerek}\n"