from os import system

kezdo:int=None
vegso:int=None
eredmeny1:int=0

print("Kérem a kezdő értéket:",end='')
kezdo=int(input().strip())

print("Kérem a végső értéket:",end='')
vegso=int(input().strip())

system('cls')
if(kezdo % 3 == 1):
    kezdo +=2
elif(kezdo % 3 == 2):
    kezdo +=1
for i in range(kezdo, vegso+1, 3):
    eredmeny1 = eredmeny1+1
print(f"A számok darabszáma:{eredmeny1}")