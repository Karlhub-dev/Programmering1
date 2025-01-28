n=0

while True:
    n+=1
    e=(1+1/n)**n
    
    if n==100000000:
        break
print(e)