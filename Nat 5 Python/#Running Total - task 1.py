# Running Total - task 1

total = 0

for months in range (12) :
    MonthlySavings = int(input("Enter your savings for this month: "))
    total = total + MonthlySavings
    print ("Your total savings currently are £",total,)