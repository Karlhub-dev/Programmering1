import random
import time

color=["♠️", "♥️", "♦️", "♣️"]
value=["E", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K"]
kortlekList=[] 
for loop in range(3): 
    for colorloop in range(4): 
        for valueloop in range(13):
            kortlek=[]
            kortlek.append(color[colorloop])
            kortlek.append(value[valueloop])
            kortlekList.append(kortlek)
random.shuffle(kortlekList)
###########################################################
# Skapar tre kortlekar där varje kort är en separat lista #
###########################################################

def cvalue(kort1): 
    kort=kort1[1]
    if kort=="E":
        cvalue=11
    elif kort=="Kn":
        cvalue=10
    elif kort=="D":
        cvalue=10
    elif kort=="K":
        cvalue=10
    else:
        cvalue=int(kort)
    return(cvalue)
###############################################################
# Omvandlar klädda kort till en int och vanliga kort till int #
###############################################################

def handprint(hand):
    antalc=len(hand)
    kortmening=""
    for cardnum in range(0, antalc):
        kort1=hand[cardnum]
        color = str(kort1[0])
        value = str(kort1[1])
        kort1= color + "  " + value
        kortmening+=kort1
    return(kortmening)
def cprint(kort1):
    color = str(kort1[0])
    value = str(kort1[1])
    kort1= color + "  " + value
    return(kort1)
###########################################
# Omvandlar korten från lista till sträng #
###########################################

def val(): #Felkollar frågan "slå eller stå?"
    try:
        val=str(input("Vill du slå eller stå?\n"))
    except ValueError:
        val()
    return(val)  

def val2(): #Felkollar startfrågan"
    try:
        spelstart = str(input("Hej där! Vill du spela lite Black Jack? Vem vet, du kanske vinner stort idag "))
    except ValueError:
        val2()
    return(spelstart)  

def main(money):

    playerhand=[]
    dealerhand=[]
    playerhand.append(kortlekList.pop(0))
    dealerhand.append(kortlekList.pop(0))
    ################################################################################
    # Tar två kort från kortlekarna och appendar till spelarens och dealerns hand #
    ################################################################################
    

    print("Du har", handprint(playerhand))  
    time.sleep(1.5) 
    print("Dealern har", handprint(dealerhand))
    time.sleep(1.5)
    playerhand.append(kortlekList.pop(0))
    dealerhand.append(kortlekList.pop(0))
    print("Du har", handprint(playerhand))
    ###################################################################################
    # Berättar vad spelaren och dealern har för startkort samt appendar två kort till #
    ###################################################################################

    
    playercvalue = (cvalue(playerhand[0])+cvalue(playerhand[1]))
    dealercvalue = (cvalue(dealerhand[0])+cvalue(dealerhand[1]))
    print(playercvalue)
    print(dealercvalue)


    while True:

        if playercvalue == 21:
                print("BLACKJACK!!")
                break
        

        val1=val()
        if val1 == "slå":

            # Ger spelaren ett till kort #
            playerhand.append(kortlekList.pop(0))
            print("Du får...")
            time.sleep(1.5)
            print(cprint(playerhand[-1]))
            time.sleep(1)
            print("Du har", handprint(playerhand))
            playercvalue += cvalue(playerhand[-1])
            print(playercvalue)

            # Kollar om spelaren fått blackjack eller blivt tjock #
            if playercvalue > 21:
                print("HAHA! Du blev tjock, casinot tar dina pengar")
                money=0
                break
            elif playercvalue == 21:
                print("Dina korts värde är 21, grattis")
                money=2*money
                break


        elif val1 == "stå":
            print("Dealern har...")
            time.sleep(1.5)
            print(handprint(dealerhand))

            while True:
                if dealercvalue > 21:
                    print("Dealern blev tjock! Du vinner!")
                    money=2*money
                    break
                elif dealercvalue == 21 and playercvalue != 21:
                    print("Dealern har blackjack! Du förlorar")
                    money=0
                    break
                elif dealercvalue == 21 and playercvalue == 21:
                    print("Det blev lika, du får tillbaka dina pengar")
                    break
                elif dealercvalue >= 17:
                    break
                dealerhand.append(kortlekList.pop(0))
                print("Dealern får...")
                time.sleep(1.5)
                print(cprint(dealerhand[-1]))
                time.sleep(1)
                print("Dealern har", handprint(dealerhand))
                dealercvalue += cvalue(dealerhand[-1])
                print(dealercvalue)
    #####################################################################
    # Ger dealern kort och kollar om den får blackjack eller blir tjock #
    #####################################################################

            time.sleep(1.5)
            if dealercvalue >= 21:
                break
            elif dealercvalue > playercvalue:
                print("Du förlorade! Casinot tar dina pengar")
                money=0
                break
            elif playercvalue > dealercvalue:
                print("Du vann!")
                money=2*money
                break
            elif playercvalue == dealercvalue:
                print("Det blev lika, du får tillbaka dina pengar")

    return(money)
            





spelstart=val2

if spelstart == "ja":
    print("Roligt!")
    time.sleep(1.5)
    bank = float(input("Hur mycket pengar vill du ta med dig till bordet?"))
    time.sleep(1)
    print("Låt oss börja...")

    while True:
        bet=float(input("Hur mycket bettar du?"))
        time.sleep(1.5)
        print("Okej, då får du dina kort")
        time.sleep(1.5)

        bank-=bet
        bank+=main(bet)

        print("Du har nu", bank, "kr till godo")

        fortsätta=input("Vill du fortsätta")
        if fortsätta == "nej":
            break
        

    







    






    
