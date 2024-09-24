Listsize=int(input("Hur många tal vill du sortera? "))
numList=[]
for i in range(1,Listsize+1):
    num=float(input("Skriv ett tal "))
    numList.append(num)
    numList.sort()
print(numList)
