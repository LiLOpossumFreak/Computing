#Structure Diagram Practise 1 - Party Cost

child_buffet = 2

choice = str(input("Is cake required?"))
if choice == "yes" or "Yes" :
    cake = 15
if choice == "No" or "no" :
    cake = 0

adults = int(input("How many adults are there?"))
children = int(input("How many children are there?"))

diet = []
for index in range(children):
    requirements = str(input("List [insert child] dietary requirements here:"))
    diet.append(requirements)

if adults + children >20 :
    venue = 0
else :
    venue = 50

cost = child_buffet * children + venue + cake
print("The cost of your party is £",cost,)