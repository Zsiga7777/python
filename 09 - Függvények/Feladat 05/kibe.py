def bekeres()->str:
    szoveg:str=None
    temp:str = None
    isszoveg: bool = False

    while ((szoveg == None) or isszoveg== False or len(szoveg) < 2):
        print("Kérek egy szót:", end='')
        temp = input()
        isszoveg = temp.isalpha()

        if (isszoveg):
            szoveg = (temp)
        else:
            print("Nem szót adott meg.")
    return szoveg

def kiiras(a:int)->None:
    print(f"A két szónak {a} Db karaktere eggyezik meg.")