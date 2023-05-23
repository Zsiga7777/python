from student import *
def atlagSztamitas(students:List[Student])->float:
    osszeg:float=0
    for student in students:
        osszeg+=student.atlag
    
    return osszeg/len(students)

def legnyagobbSzamitas(students:List[Student])->Student:
    legnyagobb:Student=students[0]
    for i in range(1,len(students),1):
        if(legnyagobb.atlag < students[i].atlag):
            legnyagobb=students[i]
    
    return legnyagobb

def atlagFeletti(students:List[Student], atlag:float)->List[Student]:
    tanulok:List[Student]=[]
    for tanulo in students:
        if (tanulo.atlag >= atlag):
            tanulok.append(tanulo)
    return tanulok