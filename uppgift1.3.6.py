num=int(input("Hur många tal vill du ha i tabellen? "))


for i in range(1,num+1):

    print(str(i), end=" ")
    print(str(i**2).rjust(10), end=" ")
    print(str(i**3).rjust(10))