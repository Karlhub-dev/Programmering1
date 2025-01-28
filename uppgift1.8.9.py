def menu(): 
    print("1: Addition")
    print("2: Subtraktion")
    print("3: multiplikation")
    print("4: Divition")

    choice = input("Välj i menyn ")

    try:
        choice = int(choice)
    except ValueError:
        print("Fel inmatning")
        choice = 0

    
    if choice >=1 and choice <=4:
        return(choice)
        
    else:
        return(False)
    
while True:
    val=menu()
    while not val:
        val=menu()

        
    if val == 1:
        num1=float(input("Vad är ditt första tal? "))
        num2=float(input("Vad är ditt andra tal? "))
        print("Summan av dina tal är", round((num1-num2),2))

    elif val ==2:
        num1=float(input("Vad är ditt första tal? "))
        num2=float(input("Vad är ditt andra tal? "))
        print("Skillnaden mellan dina tal är", round((num1-num2),2))

    elif val ==3:
        num1=float(input("Vad är ditt första tal? "))
        num2=float(input("Vad är ditt andra tal? "))
        print("Produkten av dina tal är", round((num1*num2),2))

    elif val ==4:
        num1=float(input("Vad är ditt första tal? "))
        num2=float(input("Vad är ditt andra tal? "))
        print("Kvoten av dina tal är", round((num1-num2),2))
    
    fort = input("")