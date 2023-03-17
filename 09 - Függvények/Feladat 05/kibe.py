def bekeres()->str:
    szoveg:str=None
    temp:str = None
    isszoveg: bool = False

    while ((szoveg == None) or isszoveg== False or len(szoveg) < 2):
        print("Kérek egy szót:", end='')
        temp = input().lower()
        isszoveg = temp.isalpha()

        if (isszoveg):
            szoveg = (temp)
        else:
            print("Nem szót adott meg.")
    return szoveg

def kiiras(db:int)->None:
    print(f"A két szónak {db} Db karaktere eggyezik meg.")