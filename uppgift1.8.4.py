def moms():
    kostnad=float(input("Vad kostar saken utan skatt? "))
    momstillägg=float(input("Vad är momsen i procent? "))
    kostnadmm=kostnad*(1+momstillägg/100)
    return(kostnadmm)

print("Pristen blir", moms(), "kr")
