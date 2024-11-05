

delList=[]

while True:

    menu=input("1: Mata in deltagare\n2: Visa alla deltagare\n3: Sök deltagare\n4: Mata in resultat\n5: Avsluta\nVälj i menyn:")

    if menu=="1":

        deltagare={"namn":"", "handicap":0, "resultat":""}
    
        deltagare["namn"]=input("Vad heter spelaren? ")
        
        deltagare["handicap"]=int(input("Vad är spelarens handicap? "))

        delList.append(deltagare)

    elif menu=="2":
        print(delList)

    elif menu=="3":

        search=input("Namn? ")

        for person in delList:
            if person["namn"]==search:
                print(person)

        

    elif menu=="4":

        for person in delList:

            p=str(person["namn"])

            print("Vad fick", p)
            presult=int(input("för resultat? "))
            
            person["resultat"]=presult-person["handicap"]
        
        print("")
        for result in sorted(delList, key=lambda k: k["resultat"]):
            print(str(result["namn"]), "resultat är", str(result["resultat"]))
        print("")

    elif menu=="5":
        break






























