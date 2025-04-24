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


def value(kort1): 
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

playerhand=[]
dealerhand=[]
playerhand.append(kortlekList.pop(0))
dealerhand.append(kortlekList.pop(0))
################################################################################
# Tar två kort från kortlekarna och appendar till spelarens och dealerns hand #
################################################################################


print("Spelet har börjat...")
time.sleep(1.5)
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


def val(): #Felkollar frågan "slå eller stå?"
    try:
        val=str(input("Vill du slå eller stå?\n"))
    except ValueError:
        val()
    return(val)  
  
playercvalue = (value(playerhand[0])+value(playerhand[1]))
dealercvalue = (value(dealerhand[0])+value(dealerhand[1]))
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
        playercvalue += value(playerhand[-1])
        print(playercvalue)

        # Kollar om spelaren fått blackjack eller blivt tjock #
        if playercvalue > 21:
            print("HAHA! Du blev tjock, casinot tar dina pengar")
            break
        elif playercvalue == 21:
            print("Dina korts värde är 21, grattis")
            break


    elif val1 == "stå":
        print("Dealern har...")
        time.sleep(1.5)
        print(handprint(dealerhand))

        while True:
            if dealercvalue > 21:
                print("Dealern blev tjock! Du vinner!")
                break
            elif dealercvalue == 21:
                print("Dealern har blackjack! Du förlorar")
                break
            elif dealercvalue >= 17:
                break
            dealerhand.append(kortlekList.pop(0))
            print("Dealern får...")
            time.sleep(1.5)
            print(cprint(dealerhand[-1]))
            time.sleep(1)
            print("Dealern har", handprint(dealerhand))
            dealercvalue += value(dealerhand[-1])
            print(dealercvalue)
#####################################################################
# Ger dealern kort och kollar om den får blackjack eller blir tjock #
#####################################################################

        time.sleep(1.5)
        if dealercvalue > 21:
            break
        elif dealercvalue > playercvalue:
            print("Du förlorade! Casinot tar dina pengar")
            break
        elif playercvalue > dealercvalue:
            print("Du vann!")
            break
        elif playercvalue == dealercvalue:
            print("Det blev lika, du får tillbaka dina pengar")

        

    
#########################################
# Frågar om spelaren vill slå eller stå #
#########################################

print("\n")






    






    
