# 2023 Assignment Task 1 Q1b

Journey_Stage_Costs = []
totalMiles = 0
totalCost = 0

numStations = int(input("How many charging stations will you go to in your journey? "))
startMiles = int(input("What is your mileage for the begining of your journey? "))

#Calculate & store the cost of each journey stage + display cost of each journey stage
for stations in range (numStations) :
    currentMiles = int(input("What's your current mileage? "))
    kW_Rating = int(input("What's the kW rating for the current charging station? "))
    while kW_Rating != 7 and kW_Rating != 22 and kW_Rating != 50:
        kW_Rating = int(input("ERROR INVALID INPUT What's the kW rating for the current charging station? "))
    if kW_Rating == 7:
        pricePerMile = 0
    elif kW_Rating == 22:
        pricePerMile = 0.005
    else:
        pricePerMile = 0.01
    milesTravelled = currentMiles - startMiles
    totalMiles = totalMiles + milesTravelled
    startMiles = currentMiles
    journeyStageCost = pricePerMile * milesTravelled
    Journey_Stage_Costs.append(journeyStageCost)

station = 0
for index in range (numStations) :
    totalCost = totalCost + Journey_Stage_Costs[index]
    stations = stations +1
    print("The cost for charging station",station,"is £",round(Journey_Stage_Costs[index],2))

#Display total miles and total cost
print("The total cost for your journey is £",round(totalCost,2)," and you travelled a total of ",round(totalMiles,2)," miles.")