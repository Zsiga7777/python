def devziaKonvert(osszeg:float, mertekEgyseg:str)->float:
    eredmeny:float=0
    usd:int = 360
    chf:int = 380
    jpy:float = 2.62
    if(mertekEgyseg == "USD"):
        eredmeny = osszeg/usd
    elif(mertekEgyseg == "CHF"):
        eredmeny = osszeg/chf
    else:
        eredmeny =osszeg/jpy
    
    return eredmeny

def euroKonvert(devizaErteke:float, mertekEgyseg:str)->float:
    eredmeny:float=0
    usd:int = 0.8
    chf:int = 0.55
    jpy:float = 0.75
    if(mertekEgyseg == "USD"):
        eredmeny = devizaErteke*usd
    elif(mertekEgyseg == "CHF"):
        eredmeny = devizaErteke*chf
    else:
        eredmeny =devizaErteke*jpy
    
    return eredmeny
