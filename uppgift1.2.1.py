ar=int(input("Hur mycket kostar ett årskort i kr? "))
biljett=int(input("Hur mycket kostar en biljetti kr? "))

antal=int(input("Hur många dagar har du tänkt gymma totalt under året? "))

res=biljett*antal

if res < ar:
    print("Du borde köpa biljetter, den totala kostnaden på ett år blir då", res, "kr istället för", ar, "kr")
elif res > ar:
    print("Du borde köpa ett årskort, att köpa biljetter hade kostat dig", res, "kr istället för", ar, "kr")
else:
    print("Det kostar lika mycket att köpa ett årskort som att köpa biljetter")



















