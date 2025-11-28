#Temperature Checker - level 3

from dataclasses import dataclass
@dataclass
class stuff():
    day : float = 0
    dayTemp : int = 0

TEMP = [stuff() for index in range(14)]


#----- Subroutines ------------------

def getTemps ():
   TEMP = [stuff() for index in range(14)]
   for index in range(14):
       TEMP[index].dayTemp = float(input("Please input the temperature for this day in Celcius: "))
       while TEMP[index].dayTemp < -20 or TEMP[index].dayTemp > 50 :
          TEMP[index].dayTemp = float(input("TEMPERATURE MUST BE BETWEEN -20C and 50C. Please input the temperature for this day: "))
       TEMP[index].day = index + 1
   return TEMP

def getmin(TEMP):
   min = TEMP[0].dayTemp
   for index in range(14):
      if TEMP[index].dayTemp < min :
         min = TEMP[index].dayTemp
   return min


def getmax(TEMP):
    max = TEMP[0].dayTemp
    for index in range (14):
      if TEMP[index].dayTemp > max :
         max = TEMP[index].dayTemp
    return max

def displayTemps(TEMP,min,max):
   for index in range(14):
    if index < 8 :
        print("The temperature on day ",TEMP[index].day," was ",TEMP[index].dayTemp," degrees Celcius.")
    else :
       print("The temperature on day ",TEMP[index].day," was ",TEMP[index].dayTemp," degrees Celcius.")
       print("There was a",TEMP[index].dayTemp-TEMP[index-7].dayTemp,"difference in temperature compared to this day last week.")
   print("The lowest temperature in the last 2 weeks was",min,"and the highest was",max)

def getAvgTemp(TEMP):
   totalTemps = 0
   for index in range(14):
      totalTemps = totalTemps + TEMP[index].dayTemp
   avgTemp = totalTemps/14
   print("The average temperature this week was ",avgTemp," degrees Celcius.")
   return avgTemp

def fileWrite(avgTemp):
   with open("higher/SDD/avgTemps.txt","w") as wfile:
      wfile.write(avgTemp)

#----------- Main Program --------------

TEMP = getTemps()
min  = getmin(TEMP)
max = getmax(TEMP)
displayTemps(TEMP,min,max)
avgTemp = getAvgTemp(TEMP)
fileWrite(avgTemp)
