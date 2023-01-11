max:int=None

print("Kérek egy számot:",end ='')
max = int(input().strip())

for i in range(0, max+1, 1):
    for j in range(1, i+1):
        print(f"{j}  ", end='')
    print()