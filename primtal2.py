import math

while True:

    talet=int(input("Skriv ett tal: "))
    ftalet=talet
    talList=[]
    sqrtalet=round(math.sqrt(talet))+1
    d=2

    if talet==1:
        break

    while True:
        
        print(d)

        if talet%d==0:

            talet=talet/d

            talList.append(round(d))


        else:
            if d==2:
                d+=1
            else:
                d+=2

        mult=1

        for i in talList:
            mult=mult*i

        if mult==ftalet:
            break
    
        elif d>=sqrtalet:
            if talet>1:
                talList.append(round(talet))
            break
        

    print(talList)


























