szam:float=None
temp:str = None
isSzam: bool = False
tempMasolat :str = None

while ((szam == None) or (szam < 0 or szam >= 9)):
    print("Kérek egy számot 0 és 9 között:", end='')
    temp = input()
    tempMasolat = temp.replace(".", "").replace("-","")
    isSzam = tempMasolat.isnumeric()

    if (isSzam):
        szam = float(temp)
    else:
        print("Nem számot adott meg.")
print (szam)