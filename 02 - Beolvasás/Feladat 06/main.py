from os import system

favouriteMovie:str=None
releaseDate:int=None
director:str=None
mainCharacterName:str=None

print("Kérem a kedvenc filmjének címét: ", end="")
favouriteMovie=str(input())

print("Kérem a megjelenési dátumát:", end="")
releaseDate=int(input())

print("Kérem a rendező nevét:",end="")
director=str(input())

print("Kérem a főszerepéő nevét:", end="")
mainCharacterName=str(input())

system('cls')

print(F"{releaseDate}-ban {director} rendezésében megjelent a/az {favouriteMovie} című film {mainCharacterName} főszereplésével!\n")