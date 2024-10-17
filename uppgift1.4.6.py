List=[]
num=0

while True:

    menu=input("1: lägg till tal i lista \n2: Kolla vilket tal som är störst\n3: Avsluta\n")

    if menu == "1":
        tal=float(input("Lägg till ett tal: "))
        List.append(tal)
        num+=1
    
    elif menu == "2":
        sort=List.sort
        print("Det största talet i listan är", List[num-1])
    
    elif menu == "3":
        break































