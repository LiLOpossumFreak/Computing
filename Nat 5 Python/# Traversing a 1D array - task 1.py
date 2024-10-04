# Traversing a 1D array - task 1

DailyTemps = []
total = 0

for days in range (7) :
    temp = int(input("Enter todays temperature: "))
    DailyTemps.append(temp)

for index in range (7) :
    total = total + DailyTemps[index]

average = total/7

print("The average daily temperature for this week was ",round(average,2),"degrees celcius")