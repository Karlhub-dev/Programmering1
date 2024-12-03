import math
talet=int(input("Skriv ett tal: "))

numList=[]

for n in range(2, talet):

    #Kollar om n är ett primtal#
    ifprime=True
    for d in range(2,round(math.sqrt(n))+1):
        if n%d==0:
            ifprime=False

    #Om n är ett primtal#
    if ifprime:        
        numList.append(n)

print(numList)
            

        









