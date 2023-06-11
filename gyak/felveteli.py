print("Adja meg a magyar nyelv jegyet: ",end='')
magyarJegy:int=int(input())

print("Adja meg a matematika nyelv jegyet: ",end='')
matekJegy:int=int(input())

if((magyarJegy <1 or magyarJegy >5) and (matekJegy<1 or matekJegy >5)):
    print("A magyar nyelv és matematika jegy érvénytelen!")
elif(magyarJegy <1 or magyarJegy >5):
    print("A magyar nyelv jegy érvénytelen!")
elif(matekJegy<1 or matekJegy >5):
    print("A matematika jegy érvénytelen!")