men=input("Skriv en mening: ")
countmen=men.split(" ")
rList=[]

for i in range(0, len(countmen)):
    ord=countmen[i]
    ordsize=len(ord)
    if ordsize >= 5:
         rList.append(countmen[i])

print("Din mening består av", len(countmen), "ord där", len(rList), "är mer än 5 bokstäver långa")


























