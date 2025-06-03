def val3(): #Felkollar frågan "hur mycket pengar tar du med till bordet?"
    val3=str(input("Hur mycket pengar vill du ta med dig till bordet? "))
    value=""
    for tecken in val3:
        if tecken.isdigit():
            value += tecken
    val3=float(value)
    return(val3)

print(val3())