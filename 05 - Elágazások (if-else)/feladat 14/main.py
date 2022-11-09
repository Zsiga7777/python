from  os import system

x:int=None
y:int=None
z:int=None

print("Kérem az x-et számot:",end="")
x=int(input())

print("Kérem az y-t számot:",end="")
y=int(input())

print("Kérem a z-t számot:",end="")
z=int(input())

system('cls')

if ( x%y ==0 and x%z == 0):
    print("Az x osztható z-vel és y-al is")

elif ( x%y ==0 ):
    print("Az x csak y-al osztható ")

elif ( x%z == 0):
    print("Az x csak z-vel osztható ")

else:
    print("Az x sem y-al sem z-vel nem osztható.")