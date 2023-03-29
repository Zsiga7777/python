def bekeresMertekegyseg()->str:
    mertegegyseg:str=None
    temp:str = None
    ismertegegyseg: bool = False

    while ((mertegegyseg == None) or ismertegegyseg== False or len(mertegegyseg) > 1 or (mertegegyseg != "K" and mertegegyseg != "F")):
        print("Kérek a cél mértékegysséget (K = Kelvin, F = FaFahrenheit):", end='')
        temp = input().upper()
        ismertegegyseg = temp.isalpha()

        if (ismertegegyseg):
            mertegegyseg = (temp)
        else:
            print("Nem mértékegységet meg.")
    return mertegegyseg

def bekeresSzam()->float:
    szam:str=None
    temp:str = None
    tempMasolat:str = None
    isSzam: bool = False

    while ((szam == None) or isSzam== False ):
        print("Kérek egy hőmérsékletet C-ben:", end='')
        temp = input()
        tempMasolat = temp.replace("-", "").replace(".","")
        isSzam = tempMasolat.isnumeric()

        if (isSzam):
            szam = float(temp)
        else:
            print("Nem hőmérsékleti értéket adott meg.")
    return szam

def kiiras(homersekletEredeti:float, homersekletAtvaltott:float, mertekEgyseg:str)->None:
    print(f"{homersekletEredeti} Celsius = {homersekletAtvaltott}-{mertekEgyseg}-al.")