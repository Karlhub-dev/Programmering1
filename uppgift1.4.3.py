meningList= []
sum = 0
num=0

for i in range(1,6):
    mening=input("Skriv en mening ")
    size = len(mening)
    sum += size
    num += 1
    meningList.append(size)
    if size > (meningList[num-1]):
        print(mening)

meningList.sort()
print(meningList)














