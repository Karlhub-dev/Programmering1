
numList=[]
listsize=0
nlistsize=0
for i in range(1,6):
    num=float(input("Skriv ett tal "))
    numList.append(num)
    numList.sort()
    listsize+=num
    nlistsize+=1

print(numList)
print("Medelvärdet av dina tal är", round(listsize/nlistsize,2), "\nMedianen är", numList[2])

