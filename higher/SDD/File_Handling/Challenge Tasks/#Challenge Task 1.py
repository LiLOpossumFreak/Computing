#Challenge Task 1

def getTemps():
    temps = []
    with open("higher/SDD/File_Handling/Challenge Tasks/temperatures.txt") as readfile:
        line = readfile.readline().rstrip('\n')
        while line:
            temps.append(line)
            line = readfile.readline().rstrip('\n')
    return temps



def getAverage(temps):
    totalTemps = 0
    for index in range(len(temps)):
        totalTemps = totalTemps + int(temps[index])
    averageTemp = totalTemps/len(temps)
    return averageTemp



# ------ Main Program ----------------------------------

temps = getTemps()
avgTemps = getAverage(temps)
print("The average temperature this week was ",avgTemps," degrees Celcius.")

