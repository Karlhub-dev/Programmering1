print("1: Lägg till temperaturmätning\n2: Skriv ut alla temperaturer och medeltemperatur\n3: Ta bort temperaturmätning\n4. Avsluta")

tempList=[]
average=0
naverage=0

loop=True
while loop:
   
   menu=input("Välj i menyn ")

   if menu=="1":
      temp=float(input("Lägg till tempraturmätning: "))
      tempList.append(temp)
      average+=temp
      naverage+=1

   if menu=="2":
      print("Här är alla temperaturmätningar", tempList)
      print("Medeltemperaturen är", average/naverage)

   if menu=="3":
      detemp=float(input("Ta bort temperaturmätning: "))
      if detemp in (tempList):
         tempList.remove(detemp)
      else:
         print(detemp, "finns inte i listan")

   if menu=="4":
      break
      
print(tempList)




      



   










