max:int=None

print("Kérek egy számot:",end ='')
max = int(input().strip())

for i in range(max, 1 , -1):
    for j in range(i, 0 , -1):
        print(f"{j} ", end='')
    print()
print(1)