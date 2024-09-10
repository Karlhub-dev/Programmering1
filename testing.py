ord=str(input("Skriv en meningen eller ett ord "))
if ord.count(" ")>0:
    a="Din mening är en palondrom"
elif ord.count(" ")==0:   
    a="Ditt ord är en palondrom"
ord=ord.strip(" ")


if ord == ord[::-1]:
    print(a)






















