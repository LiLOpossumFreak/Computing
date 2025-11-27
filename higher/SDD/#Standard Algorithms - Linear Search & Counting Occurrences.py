#Standard Algorithms - Linear Search & Counting Occurrences - Part 1

#Task 1
ownsAnIphone = ["Yes","No","No","No","Yes","Yes","Yes","Yes"]
counter = 0
numIphones = "Yes"

for index in range(len(ownsAnIphone)):
    if numIphones == ownsAnIphone[index]:
        counter = counter + 1
print(counter,"people own iPhones.")


#Task 2
petPurchased = ["dog","dog","cat","rabbit","hamster","cat","hamster","budgie"]
counter = 0
pet = "hamster"
position = 0

for index in range(len(petPurchased)):
    if pet == petPurchased[index]:
        position = counter
    counter = counter + 1

if position != 0:
    print(position)
else:
    print("No hamsters purchased :(")


#Task 3
petPurchased = ["dog","dog","cat","rabbit","hamster","cat","hamster","budgie"]
counter = 0
pet = "hamster"
position = []

for index in range(len(petPurchased)):
    if pet == petPurchased[index]:
        position.append(counter)
    counter = counter + 1

if position != 0:
    print(position)
else:
    print("No hamsters purchased :(")
