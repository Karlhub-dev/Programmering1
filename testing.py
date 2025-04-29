import random

def cvalue(kort1): 
    kort1=list(kort1)
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

playerhand=[]

playerhand.append(kortlekList.pop(0))

    ################################################################################
    # Tar två kort från kortlekarna och appendar till spelarens och dealerns hand #
    ################################################################################

print("Spelet har börjat...")





    ###################################################################################
    # Berättar vad spelaren och dealern har för startkort samt appendar två kort till #
    ###################################################################################

print(playerhand)
playercvalue = (cvalue(playerhand[0]))

print(playercvalue)











