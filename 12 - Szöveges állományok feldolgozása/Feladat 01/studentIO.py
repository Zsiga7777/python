from typing import *
from io import open
import os
from student import Student
def tanuloBekeres()->List[Student]:
    fileName:str = "data/adatok.txt"
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    oneLine:str = None
    data:list[str]=[]
    students:List[Student]=[]
    student:Student=None

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip()
                data=oneLine.split("\t")
                student= Student()
                student.nev=data[0]
                student.atlag= float(data[1].replace(",","."))
                students.append(student)
        return students
            
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []
