def agecheck(age):
    
    if age < 18:
        return(False)
    else:
        return(True)

in_val = int(input("Hur gammal är du? "))

if agecheck(in_val):
    print("Du är myndig")
else:
    print("Baby!")