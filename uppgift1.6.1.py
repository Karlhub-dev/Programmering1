import random

tal= random.randint(1,100)

try:
    antal=int(input("Hur många gissningar vill du ha "))
except ValueError: 
    print("Fel inmatning! Måste ange ett heltal!")
    antal=int(input("Hur många gissningar vill du ha "))

i=0

if antal > 10:
    print("Haha! du får bara 10 gissningar")
    antal = 10



while i < antal:

    try:
        gis=round(int(input("Gissa vilket tal jag tänker på mellan 1 och 100 ")))
    except ValueError:
        print("Fel inmatning! Måste ange ett heltal!")
        gis=round(int(input("Gissa vilket tal jag tänker på mellan 1 och 100 ")))

    if gis < tal:
        print("För lågt")
    elif gis > tal:
        print("För högt")    
    else:
        print("Du gissade rätt! Bra jobbat! Det tog dig bara", i+1, "gissningar")
    i+=1
    if gis == tal:
        i=antal+1
    elif i == antal:
        print("Haha, du har slut på gissningar, rätt svar var", tal)
    