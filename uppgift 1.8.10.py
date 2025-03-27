def menu():
    print("1. Beräkna räntekostnad\n2. Beräkna räntekostnaden under period")

    try:
        choice = int(input("Välj i menyn: "))
    except ValueError:
        print("Fel inmatning, försök igen")
        choice = int(input("Välj i menyn: "))
    return(choice)

def rkostnad():
    belopp=float(input("Hur stort är ditt lån i kr? "))
    ränta=float(input("Vad är räntan i procent? "))
    return(belopp*(ränta/100))

    

    

while True:
    val=menu()

    if val == 1:
        print("Räntekostnaden blir", rkostnad(), "kr")
    if val == 2:
        break







