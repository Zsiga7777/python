max:int=None
lista:list =[]

print("Kérek egy számot:",end ='')
max = int(input().strip())

for i in range(1, max+1, 1):
    lista.append(i) 
    print("     ".join(map(str,lista)))