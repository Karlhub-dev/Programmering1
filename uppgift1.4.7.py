hundList={"namn":"","ras":"","vikt":""}

hundList["namn"]=input("Vad heter hunden? ")
hundList["ras"]=input("Vilken ras är hunden? ")
hundList["vikt"]=input("Hur mycket väger hunden i kg? ")

print("1: Byt något om hunden\n2: Visa hunden\n3: Avsluta")

while True:

    menu=input("Välj i menyn: ")

    if menu =="1":

        change=input("Vad vill du byta? ")

        if change=="namn":
            hundList["namn"]=input("Vad heter hunden? ")
        elif change=="ras":
            hundList["ras"]=input("Vilken ras är hunden? ")
        elif change=="vikt":
            hundList["vikt"]=input("Hur mycket väger hunden i kg? ")
        
    elif menu =="2":
        print(hundList)
    
    elif menu =="3":
        break













