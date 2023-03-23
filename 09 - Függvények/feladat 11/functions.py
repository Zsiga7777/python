def oraberSzamitas(oraSzam:str)->str:
    vegso:str= ""
    eredmeny:int=0
    fizetes:int = 1000
    for i in range (0, 5, 1):
        eredmeny = int(oraSzam.split(",")[i])*fizetes 
        if(int(oraSzam.split(",")[i]) > 40):
            eredmeny = eredmeny + ((int(oraSzam.split(",")[i])-40)*500)
        vegso += str(eredmeny) + ","
        eredmeny = 0
    return vegso

