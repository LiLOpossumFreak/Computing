#Task A3 - Standard Algorithms Input Validation

names = [ ] 
clans = [ ]

name = str(input("What is your name: "))
names.append(name)
clan = str(input("What clan are you in: "))
while clan == "Stuart" or clan == "Forbes" or clan == "Douglas" or clan == "Gordon" :
    clans.append(clan)
else :
    clan = str(input("ERROR What clan are you in: "))
