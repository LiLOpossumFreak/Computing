# 2023 Assignment Task 1 Q1b

Journey_Stage_Costs = []
startMiles = 0
totalMiles = 0
totalCost = 0

numStations = int(input("How many charging stations will you go to in your journey? "))

#Calculate & store the cost of each journey stage + display cost of each journey stage
for stations in range (numStations) :
    currentMiles = int(input("What's your current mileage? "))
    kW_Rating = int(input("What's the kW rating for the current charging station? "))
    while kW_Rating != 7 and kW_Rating != 22 and kW_Rating != 50:
        kW_Rating = int(input("ERROR INVALID INPUT What's the kW rating for the current charging station? "))
    while kW_Rating == 7:
        pricePerMile = 0
    while kW_Rating == 22:
        pricePerMile = 0.005
    while kW_Rating == 50:
        pricePerMile = 0.01
    totalMiles = totalMiles + currentMiles
    milesTravelled = currentMiles - startMiles
    startMiles = currentMiles
    journeyStageCost = pricePerMile * milesTravelled
    Journey_Stage_Costs.append(journeyStageCost)
    print("The cost for this charging station is £",ROUND(journeyStageCost,2))

for index in range (numStations) :
    totalCost = totalCost + Journey_Stage_Costs[index]

#Display total miles and total cost
print("The total cost for your journey is £",ROUND(totalCost,2)," any you travelled a total of ",ROUND(totalMiles,2)," miles.")
Journey_Stage_Costs = []
startMiles = 0
totalMiles = 0
totalCost = 0

numStations = int(input("How many charging stations will you go to in your journey?"))

#Calculate & store the cost of each journey stage + display cost of each journey stage
for stations in range (numStations) :
    currentMiles = int(input("What's your current mileage?"))
    kW_Rating = int(input("What's the kW rating for the current charging station?"))
    while kW_Rating == 7:
        pricePerMile = 0
    while kW_Rating == 22:
        pricePerMile = 0.005
    while kW_Rating == 50:
        pricePerMile = 0.01
    while kW_Rating != 7 or kW_Rating != 22 or kW_Rating != 50:
        kW_Rating = int(input("ERROR INVALID INPUT What's the kW rating for the current charging station?"))
    totalMiles = totalMiles + currentMiles
    milesTravelled = currentMiles - startMiles
    startMiles = currentMiles
    journeyStageCost = pricePerMile * milesTravelled
    Journey_Stage_Costs.append(journeyStageCost)
    print("The cost for this charging station is £",ROUND(journeyStageCost,2))

for index in range (numStations) :
    totalCost = totalCost + Journey_Stage_Costs[index]

#Display total miles and total cost
print("The total cost for your journey is £",ROUND(totalCost,2)," any you travelled a total of ",ROUND(totalMiles,2)," miles.")