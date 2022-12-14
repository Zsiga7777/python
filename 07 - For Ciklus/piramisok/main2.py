max:int=None
lista:list =[]

print("Kérek egy számot:",end ='')
max = int(input().strip())

for i in range(max, 0 , -1):
    lista.append(i) 
for i in range(max, 0 , -1):
    print("\t".join(map(str,lista)))
    del lista[0]