#Running Total - task 2

total = 0

for tests in range (5) :
    TotalScore = int(input("Enter your last test score: "))
    total = total + TotalScore
    print ("Your total score is currently ",total,)