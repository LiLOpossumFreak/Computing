#Structure Diagram Practice 2 - Journey Cost

NumStations = int(input("How many charging stations will you visit: "))
startMiles = 0
index = 0
for index in range(NumStations):
    currentMiles = int(input("Enter the mileage at the current charging stations: "))
    kWRating = int(input("Enter the kW rating at the current charging station: "))

    while kWRating == 7:
        pricePerMile = 0
    while kWRating == 22:
        pricePerMile = 0.005
    while kWRating == 50:
        pricePerMile = 0.01
    milesTravelled = currentMiles - startMiles
    startMiles = currentMiles
    journeyStageCost = pricePerMile * milesTravelled
    print("The total cost for this stage of the journey was £",journeyStageCost)