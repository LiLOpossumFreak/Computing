#Temperature Checker

#Subroutines

def getTemps ():
   Temps = []
   for index in range(5):
       temp = int(input("Please input the temperature for this day in Celcius: "))
       if temp < -20 or temp > 50 :
          temp = int(input("TEMPERATURE MUST BE BETWEEN -20C and 50C. Please input the temperature for day",index,": "))
       Temps.append(temp)
   return Temps

def displayTemps(Temps):
   for index in range(5):
      print("The temperature on day ",index+1," was ",Temps[index]," degrees Celcius.")

def getAvgTemp(Temps):
   totalTemps = 0
   for index in range(5):
      totalTemps = totalTemps + Temps[index]
   avgTemp = totalTemps/5
   print("The average temperature this week was ",avgTemp," degrees Celcius.")


#----------- Main Program --------------

Temps = getTemps()
displayTemps(Temps)
getAvgTemp(Temps)
