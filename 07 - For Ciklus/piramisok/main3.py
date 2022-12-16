max:int=None
lista:list =[]
lista2:list =[]

print("Kérek egy számot:",end ='')
max = int(input().strip())

for i in range(1, max*2, 1):
    lista.append("  ") 

for i in range(1, max*2, 1):
    lista.append(i)
    lista.append("   ")  
    del lista[0]
    print("".join(map(str,lista)))