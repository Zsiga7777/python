max:int=None
lista:list =[]

print("Kérek egy számot:",end ='')
max = int(input().strip())
lista.append(\t)

for i in range(1, max+1, 1):
    lista.append(i) 
    print("\t".join(map(str,lista)))