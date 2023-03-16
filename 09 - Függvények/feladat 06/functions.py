def fokKonvert(homerseklet:float, mertekEgyseg:str)->float:
    eredmeny:float=0
    if(mertekEgyseg == "K"):
        eredmeny = homerseklet + 273.15
    else:
        eredmeny =9/5*homerseklet+32
    
    return eredmeny
