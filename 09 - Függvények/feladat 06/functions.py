def fokKonvert(a:float, b:str)->float:
    eredmeny:float=0
    if(b == "K"):
        eredmeny = a + 273.15
    else:
        eredmeny =9/5*a+32
    
    return eredmeny
