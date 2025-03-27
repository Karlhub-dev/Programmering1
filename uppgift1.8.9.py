def menu(): 
    print("1: Addition")
    print("2: Subtraktion")
    print("3: multiplikation")
    print("4: Divition")

    try:
        choice = int(input("Välj i menyn "))
    except ValueError:
        print("Fel inmatning! Välj en av siffrorna i menyn")
        choice = int(input("Välj i menyn "))

    
    if choice >=1 and choice <=4:
        return(choice)
        
    else:
        return(False)
    
def mathadd(add1,add2):
    return(add1+add2)
def mathsub(sub1,sub2):
    return(sub1-sub2)
def mathmul(mul1,mul2):
    return(mul1*mul2)
def mathdiv(div1,div2):
    return(div1/div2)

choice=menu()

num= float(input("Vad är ditt första tal "))
num2= float(input("Vad är ditt första tal "))
if choice==1:
    print("Summan av dina tal är", mathadd(num,num2))
elif choice==2:
    print("Skillnaden mellan dina tal är",mathsub(num,num2))
elif choice==3:
    print("Produkten av din tal är", mathmul(num,num2))
elif choice==4:
    print("Kvoten av dina tal är", mathdiv(num,num2))


