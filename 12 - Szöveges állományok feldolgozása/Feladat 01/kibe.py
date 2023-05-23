from student import *
import os
def kiiras(students:List[Student],fileNev:str)->None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output/"
    fileFullPath: str = os.path.join(basepath, fileNev)
    try:
        with open(fileFullPath, encoding="utf-8", mode="w") as file:
            for student in students:
                file.write(f"{student}\n")
    except FileNotFoundError as ex:
        print(F"{ex.filename} nem található!")