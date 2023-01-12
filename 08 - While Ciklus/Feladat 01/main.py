szam:int=None

print("Kérek egy számot 0 és 9 között:", end='')
szam= int(input())

while (szam <=0 or szam>10):
    print("Kérek egy számot 0 és 9 között:", end='')
    szam= int(input())
print (szam)