meningList= []
sum = 0
num=0
mensize=0


for i in range(1,6):
    mening=input("Skriv en mening ")
    size = len(mening)
    sum += size
    num += 1
    meningList.append(size)
    if size > mensize:
        mensize=size
        rmening=mening
    

print("Den längsta meningen var", rmening, "\nMedellängden på meningarna är", round(sum/num,2), "tecken långa")















