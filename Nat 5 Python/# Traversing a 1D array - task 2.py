# Traversing a 1D array - task 2

DailyFoodWeights = []
total = 0

for days in range (5) :
    weight = int(input("Enter the amount of food your dog was given today in grams: "))
    while weight <0 or weight >300 :
        weight = int(input("ERROR Enter the amount of food your dog was given today in grams: "))
    DailyFoodWeights.append(weight)

for index in range (5) :
    total = total + DailyFoodWeights[index]

print("The total amount of food your dog was given in the last 5 days is ",total,"grams")