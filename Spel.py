import random
while True:

    menu=input("Vilket spel vill du spela\n1: Gambling\n2: Sten sax påse\n3: Blackjack\n4: Avsluta\n")

    if menu =="1":

        print("Du är nu en gambler och du börjar med 1000 kr")
        bank=1000

        while True:

            while True:

                bet=float(input("Hur mycket vill du statsa? "))
                if bet > bank:
                    print("Du har inte råd")
                else:
                    break

            chance=random.randint(1,99)+random.expovariate(1)
            betchance=(1-((bet+bet/bank)/bank))*100

            if chance<=betchance:
                print("Du vann! Ditt bet dubblas")
                bank+=bet*2
                print("Du har nu", bank, "kr")

            else:
                print("Du förlorade. Casinot tar dina pengar")
                bank-=bet
                print("Du har nu", bank, "kr")

            gexit=input("Vill du fortsätta? ")

            if gexit == "nej":
                break
        
    if menu =="2":

        compcount=0
        count=0

        print("Du kommer spela sten sax påse mot en dator, lycka till.")

        for i in range(0,10):

            move=input("Vilket drag vill du göra? ")
            compgen=random.randint(1,3)
    

            if compgen==1:
                compmove="sten"
            elif compgen==2:
                compmove="sax"
            elif compgen==3:
                compmove="påse"

            print("Sten... Sax... Påse!")

            if move == compmove:
                print("Oavgjort. Båda valde", move)

            elif move == "sten" and compmove == "sax":
                print("Du vinner med sten mot sax")
                count+=1

            elif move == "sten" and compmove == "påse":
                print("Du förlorar med sten mot påse")
                compcount+=1

            elif move == "sax" and compmove == "påse":
                print("Du vinner med sax mot påse")
                count+=1

            elif move == "sax" and compmove == "sten":
                print("Du förlorar med sax mot sten")
                compcount+=1
 
            elif move == "påse" and compmove == "sten":
                print("Du vinner med påse mot sten")
                count+=1

            elif move == "påse" and compmove == "sax":
                print("Du förlorar med påse mot sax")
                compcount+=1
   

        if count > compcount:
            print("Du vann över datorn med", count, "till", compcount)

        elif count < compcount:
            print("Du förlora mot datorn med", count, "till", compcount)

        else:
            print("Matchen blev oavgjord. Båda spelare fick", count)
        
        print("\n")

    if menu == "3":

        cardList=[]
        compcardList=[]

        loop=2

        for i in range(0,loop):

            color=random.randint(1,4)
            if color==1:
                color="Klöver"
            if color==2:
                color="Ruter"
            if color==3:
                color="Hjärter"
            if color==4:
                color="Spader"

            value=random.randint(1,13)
            if value==11:
                value="Knäckt"
            elif value==12:
                value="Dam"
            elif value==13:
                value="Kung"
            elif value==1:
                value=="Ess"
            
            card=color+" "+str(value)
            cardList.append(card)

        for i in range(0,21):

            ccolor=random.randint(1,4)
            if ccolor==1:
                ccolor="Klöver"
            if ccolor==2:
                ccolor="Ruter"
            if ccolor==3:
                ccolor="Hjärter"
            if ccolor==4:
                ccolor="Spader"

            cvalue=random.randint(1,13)
            if cvalue==11:
                cvalue="Knäckt"
            elif cvalue==12:
                cvalue="Dam"
            elif cvalue==13:
                cvalue="Kung"
            elif cvalue==1:
                cvalue=="Ess"
            
            ccard=ccolor+" "+str(cvalue)
            compcardList.append(ccard)

        print("Dina kort är", cardList)
        print("Dealerna har", compcardList[0])

        move=input("Vill du fortsätta eller stanna? ")

        if move=="fortsätta":
            color=random.randint(1,4)
            if color==1:
                color="Klöver"
            if color==2:
                color="Ruter"
            if color==3:
                color="Hjärter"
            if color==4:
                color="Spader"

            value=random.randint(1,13)
            if value==11:
                value="Knäckt"
            elif value==12:
                value="Dam"
            elif value==13:
                value="Kung"
            elif value==1:
                value=="Ess"
            
            card=color+" "+str(value)
            cardList.append(card)
            print("Du har nu", cardList)


        elif move=="stanna":
            print("Dealern har", compcardList[1,2])


            


    if menu =="4":
        break

































