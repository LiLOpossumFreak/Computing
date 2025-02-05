# 2022 Assignment Task 1 Q1b

totalFoodWeight = 0
foodWeights = []

for containers in range (5):
    foodWeight = int(input("Enter the weight of food in this container: "))
    while foodWeight < 0 or foodWeight > 200 :
        foodWeight = int(input("ERROR The containers can only hold up to 200 grams. Enter the weight of food in this container: "))
    foodWeights.append(foodWeight)
    totalFoodWeight = totalFoodWeight + foodWeight

dogSize = str(input("What size is your dog, small, medium or large: "))
if dogSize == "small" and totalFoodWeight <= 110 and totalFoodWeight >= 140 :
    recommendation = "This weight of food is suitable for your small dog."
elif dogSize == "medium" and totalFoodWeight <= 330 and totalFoodWeight >= 440 :
    recommendation = "This weight of food is suitable for your medium dog."
elif dogSize == "large" and totalFoodWeight <= 690 and totalFoodWeight >= 900 :
    recommendation = "This weight of food is suitable for your large dog."
else:
    recommendation = "This weight of food is not recommended for the size of dog"

averageFoodWeight = totalFoodWeight / 5

container = 0
for weights in range (5):
    container = container+ 1
    print("The weight of food in container ",container,"is",foodWeights[index]," grams.")

print("The total weight of the food in the containers is ",totalFoodWeight)
print("The average weight of the food in each container is ",round(averageFoodWeight,1))
print(recommendation)