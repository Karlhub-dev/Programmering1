print("1: Lägg till i listan\n2: Kolla efter dubbleter\n3: Avsluta")


List=[]


loop=True
while loop:

    menu=input("Välj i menyn: ")

    if menu == "1":
        add=input("Tillägg i listan: ")
        List.append(add)

    elif menu == "2":
        print("Kollar efter dubbleter...")
        check=0
        testList=List

        for i in range(0, len(testList)-1):

            tester=testList.count(testList[i])

            if tester > 1:
                print("Det finns en dubblet i listan:", List[i])
                check+=1


        if check == 0:
            print("Det finns inga dubbleter i listan")
                

    elif menu == "3":
        break

    elif menu== "4":
        print(List)


    








