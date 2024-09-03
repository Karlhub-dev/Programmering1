import random

a=int(input("Hur många tärningar kastar du? "))
summa=0


for i in range(1, a+1):  ### när i är mellan 1 och a+1 utför koden nedan, i ökas med 1 varje gång koden utförts
    slump = random.randint(1,6) ### Variabel som slumpar en siffra mella 1-6 varje gång koden utförs
    print("Tärning", i, "visar", slump) ### Visar vad varje tärning fått för värde
    summa += slump ### Lägger ihop alla värden till en summa

print("Summan av dina", a, "tärningar är", summa)
medv = summa/a
print("Medelvärdet av dina tärningar är", round(medv, 2))














