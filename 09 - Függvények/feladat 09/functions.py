def devziaKonvert(a:float, b:str)->float:
    eredmeny:float=0
    usd:int = 360
    chf:int = 380
    jpy:float = 2.62
    if(b == "USD"):
        eredmeny = a/usd
    elif(b == "CHF"):
        eredmeny = a/chf
    else:
        eredmeny =a/jpy
    
    return eredmeny

def euroKonvert(a:float, b:str)->float:
    eredmeny:float=0
    usd:int = 0.8
    chf:int = 0.55
    jpy:float = 0.75
    if(b == "USD"):
        eredmeny = a*usd
    elif(b == "CHF"):
        eredmeny = a*chf
    else:
        eredmeny =a*jpy
    
    return eredmeny
