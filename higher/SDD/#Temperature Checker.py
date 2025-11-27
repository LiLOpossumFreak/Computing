#Temperature Checker - level 2

from dataclasses import dataclass
@dataclass
class stuff():
    day : int = 0
    dayTemp : int = 0

TEMP = [stuff() for index in range(14)]

def getTemps ():
   TEMP = [stuff() for index in range(14)]
   for index in range(14):
       TEMP[index].dayTemp = int(input("Please input the temperature for this day in Celcius: "))
       while TEMP[index].dayTemp < -20 or TEMP[index].dayTemp > 50 :
          TEMP[index].dayTemp = int(input("TEMPERATURE MUST BE BETWEEN -20C and 50C. Please input the temperature for this day: "))
       TEMP[index].day = index + 1
   return TEMP

def displayTemps(TEMP):
   for index in range(14):
    if index < 8 :
        print("The temperature on day ",TEMP[index].day," was ",TEMP[index].dayTemp," degrees Celcius.")
    else :
       print("The temperature on day ",TEMP[index].day," was ",TEMP[index].dayTemp," degrees Celcius.")
       print("There was a",TEMP[index].dayTemp-TEMP[index-7].dayTemp,"difference in temperature compared to this day last week.")

def getAvgTemp(TEMP):
   totalTemps = 0
   for index in range(14):
      totalTemps = totalTemps + TEMP[index].dayTemp
   avgTemp = totalTemps/14
   print("The average temperature this week was ",avgTemp," degrees Celcius.")


#----------- Main Program --------------

TEMP = getTemps()
displayTemps(TEMP)
getAvgTemp(TEMP)
