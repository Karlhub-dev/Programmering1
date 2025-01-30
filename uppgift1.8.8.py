def CtillF(temp):
    return(temp*1.8+32)

def FtillC(temp):
    return((temp-32)/1.8)

menu=input("1: Omvandla celsius till farenheit\n2: Omvandla farenheit till celsius\n")

if menu == "1":
    temp=float(input("Vad är temperaturen i C? "))
    print("Temperaturen i farneheit är", CtillF(temp))

if menu == "2":
    temp=float(input("Vad är temperaturen i F? "))
    print("Temperaturen i farneheit är", FtillC(temp))