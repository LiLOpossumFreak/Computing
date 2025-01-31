# 2022 Assignment Task 1 Q1b

totalFoodWeight

for 5 in range:
    foodWeight = int(input("Enter the weight of food in this container: "))
    while foodWeight < 0 or foodWeight > 200 :
        foodWeight = int(input("ERROR The containers can only hold up to 200 grams. Enter the weight of food in this container: "))
    totalFoodWeight = totalFoodWeight + foodWeight

dogSize = str(input("What size is your dog, small, medium or large: "))

averageFoodWeight = totalFoodWeight / 5

print("The average weight of the food in each container is ",round(averageFoodWeight,1))