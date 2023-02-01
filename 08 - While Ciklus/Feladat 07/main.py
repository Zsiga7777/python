kezdoErtek:str=None
kezdoErtekMasolat:str=None
vegErtek:str=None
vegErtekMasolat:str=None
leptetesMerteke:str=None
leptetesMertekemasolat:str=None


while (kezdoErtek == None or vegErtek == None or kezdoErtek >= vegErtek or leptetesMerteke>0):
    print("Kérek egy kezdőértéket:", end='')
    kezdoErtek = input()
    kezdoErtekMasolat = kezdoErtek.replace(".", "").replace("-", "")
    if(kezdoErtekMasolat.isnumeric()):
        kezdoErtek = int(kezdoErtek)

    print("Kérek egy végértéket:", end='')
    vegErtek = input()
    vegErtekMasolat = vegErtek.replace(".", "").replace("-", "")
    if(vegErtekMasolat.isnumeric()):
        vegErtek = int(vegErtek)

    print("Kérek egy léptetési mértéket(negatív):", end='')
    leptetesMerteke = input()
    leptetesMertekemasolat = leptetesMerteke.replace(".", "").replace("-", "")
    if(leptetesMertekemasolat.isnumeric()):
        leptetesMerteke = int(leptetesMerteke)

for i in range(vegErtek, kezdoErtek-1 , leptetesMerteke):
    print(i)