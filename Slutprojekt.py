import random

color=["Spader", "Hjärter", "Ruter", "Klöver"]
value=["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung"]
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
    if kort=="Ess":
        cvalue=11
    elif kort=="Knekt":
        cvalue=10
    elif kort=="Dam":
        cvalue=10
    elif kort=="Kung":
        cvalue=10
    else:
        cvalue=int(kort)
    return(cvalue)
###############################################################
# Omvandlar klädda kort till en int och vanliga kort till int #
###############################################################


playerhand=[]
dealerhand=[]
for startcards in range(2):
    playerhand.append(kortlekList.pop(0))
    
    dealerhand.append(kortlekList.pop(0))
################################################################################
# Tar fyra kort från kortlekarna och appendar till spelarens och dealerns hand #
################################################################################


print("Du har", playerhand)   
print("Dealern har", dealerhand[0])


def val(): #Felkollar frågan "slå eller stå?"
    try:
        val=str(input("Vill du slå eller stå?\n"))
    except ValueError:
        val()
    return(val)  
  
playercvalue = (value(playerhand[0])+value(playerhand[1]))
print(playercvalue)
while True:
    if playercvalue == 21:
            print("BLACKJACK!!")
            break
    val1=val()
    if val1 == "slå":
        playerhand.append(kortlekList.pop(0))
        print("Du har", playerhand)
        playercvalue += value(playerhand[-1])
        print(playercvalue)
        if playercvalue > 21:
            print("HAHA! du blev tjock, casinot tar dina pengar")
            break
        elif playercvalue == 21:
            print("BLACKJACK!!")
            break


    elif val1 == "stå":
        print("Dealern har ", dealerhand)
        break
#########################################
# Frågar om spelaren vill slå eller stå #
#########################################

print("\n")






    






    
