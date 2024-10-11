#Task A4 - Standard Algorithms Input Validation

prev = int(input("Please enter your previous meter reading: "))
current = int(input("Please enter your current meter reading: "))
while current < 0 or current > 10:
    current = int(input("ERROR Please enter your current meter reading: "))
UnitCost = int(input("Please enter the unit cost: "))