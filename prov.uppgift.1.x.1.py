def meningbearb(mening): #Bearbetar meningen och tar bort skiljetecken
    bemening1=mening.replace(".", " ")
    bemening2=bemening1.replace(",", " ")
    bemening3=bemening2.replace(":", " ")
    bemening4=bemening3.replace("?", " ")
    bemening5=bemening4.replace("!", " ")
    bemening6=bemening5.replace("  ", " ") #Vi körning kan dubbla mellanslag bildas, dessa ersätts med ett mellanslag så att split-funktionen fungerar.
    return(bemening6.rstrip())

def antalord(mening): #Räknar antalet ord i meningen efter skiljetecken tagits bort
    mening=meningbearb(mening)
    meningList=mening.split(" ") #Gör meningen till en lista med varje ord som ett separat objekt
    return(len(meningList))

def unikaord(mening): #Tar bort dubbletter av ord i listan tills varje ord är unikt
    mening=meningbearb(mening)
    meningList=mening.split(" ")
    meningList=sorted(list(set(meningList))) #Skapar de unika orden
    return(meningList)

def ordforekomst(mening): #Jämför de unika orden med alla ord och räknar hur många gånger varje unikt ord förekommer
    mening=meningbearb(mening)
    meningList=mening.split(" ")
    meningListunik=sorted(list(set(meningList)))
    numList=[]

    for i in range(0,len(meningListunik)):# Jämför och räknar
        count=0
        for o in range(0, len(meningList)):
            if meningListunik[i]==meningList[o]:
                count+=1
        if count > 0:
            numList.insert(i, count)    

    return(numList)

def langstaord(mening): #Hittar det längst ordet i meningen
    n=0
    ord=""
    mening=meningbearb(mening)
    meningList=mening.split(" ")
    mening1=sorted(list(set(meningList)))
    for i in range(0, len(mening1)):
        if len(mening1[i])>n:
            n=len(mening1[i])
            ord=mening1[i]
    return(ord)

def answer(): #Skriver alla unika ord och hur ofta de förekommer, det längsta ordet och hur många ord meningen består av
    mening1=input("Skriv en mening: ")
    retstr=""
    for t in range(0, len(unikaord(mening1))):
        retstr=retstr+"Ordet: "+ str(unikaord(mening1)[t])+ " förekommer "+ str(ordforekomst(mening1)[t])+ " gånger\n"
    retstr=retstr+ "Det längsta ordet är: "+str(langstaord(mening1))+"\nMeningen består av: "+str(antalord(mening1))+" ord"
    return(retstr)


print(answer())






