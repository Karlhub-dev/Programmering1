numList=[]

times=int(input("Hur många tal finns i listan? "))

for i in range(0, times):
    num=int(input("Lägg till ett tal: "))
    numList.append(num)

print("Kollar om listan är i storleksordning...\n")

numList2=sorted(numList)

if numList2 == numList:
    print("Talen är i storleksordning")
else:
    print("Talen är inte i storleksordning")