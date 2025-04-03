import random

    


cardList=[]
compcardList=[]

cardcount=0
ccardcount=0

for i in range(0,2):

    color=random.randint(1,4)
    if color==1:
        color="Klöver"
    elif color==2:
        color="Ruter"
    elif color==3:
        color="Hjärter"
    elif color==4:
        color="Spader"

            value=random.randint(1,13)

            cardcount+=value

            if value==11:
                cardcount-=1
                value="Knekt"
            elif value==12:
                cardcount-=2
                value="Dam"
            elif value==13:
                cardcount-=3
                value="Kung"
            elif value==1:
                cardcount+=10
                value="Ess"
        
            
            
            card=color+" "+str(value)
            cardList.append(card)
            

        for i in range(0,2):

            ccolor=random.randint(1,4)
            if ccolor==1:
                ccolor="Klöver"
            elif ccolor==2:
                ccolor="Ruter"
            elif ccolor==3:
                ccolor="Hjärter"
            elif ccolor==4:
                ccolor="Spader"

            cvalue=random.randint(1,13)

            ccardcount+=cvalue

            if cvalue==11:
                ccardcount-=1
                cvalue="Knäckt"
            elif cvalue==12:
                ccardcount-=2
                cvalue="Dam"
            elif cvalue==13:
                ccardcount-=3
                cvalue="Kung"
            elif cvalue==1:
                ccardcount+=10
                cvalue="Ess"
        
            
            ccard=ccolor+" "+str(cvalue)
            compcardList.append(ccard)

        print("Dina kort är", cardList)
        print("Dealerna har", compcardList[0])

        while True:
        
            move=input("Vill du fortsätta eller stanna? ")

            if move=="fortsätta":
                color=random.randint(1,4)
                if color==1:
                    color="Klöver"
                elif color==2:
                    color="Ruter"
                elif color==3:
                    color="Hjärter"
                elif color==4:
                    color="Spader"

           
                value=random.randint(1,13)

                cardcount+=value

                if value==11:
                    cardcount-=1
                    value="Knäckt"
                elif value==12:
                    cardcount-=2
                    value="Dam"
                elif value==13:
                    cardcount-=3
                    value="Kung"
                elif value==1:
                    cardcount+=10
                    value="Ess"
                
            
                card=color+" "+str(value)
                cardList.append(card)
                print("Du har nu", cardList)
                

            elif move=="stanna":
                break
        
        showclist=1

        while True:

            print("Dealern har", compcardList[0:showclist])

            if ccardcount>=17:
                break

            else:

                ccolor=random.randint(1,4)

                if ccolor==1:
                    ccolor="Klöver"
                elif ccolor==2:
                    ccolor="Ruter"
                elif ccolor==3:
                    ccolor="Hjärter"
                elif ccolor==4:
                    ccolor="Spader"

                cvalue=random.randint(1,13)

                ccardcount+=cvalue

                if cvalue==11:
                    ccardcount-=1
                    cvalue="Knäckt"
                elif cvalue==12:
                    ccardcount-=2
                    cvalue="Dam"
                elif cvalue==13:
                    ccardcount-=3
                    cvalue="Kung"
                elif cvalue==1:
                    ccardcount+=10
                    cvalue="Ess"
            
                ccard=ccolor+" "+str(cvalue)
                compcardList.append(ccard)
                showclist+=1
        
        print("Dealern har nu", compcardList)

        if ccardcount==21:
            print("Dealern har blackjack. Du förlorade")
        elif cardcount>=22:
            print("Dealern vart tjock. Du vann")
        
        if cardcount==ccardcount:
            print("Det vart oavgjort")
        elif cardcount>ccardcount:
            print("Du vann")
        elif ccardcount>cardcount:
            print("Du förlorade")
            
 































