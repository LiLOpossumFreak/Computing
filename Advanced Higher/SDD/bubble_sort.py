myList = [3,4,9,7,1]
swaps = 0

#Sorts into descedning order
#start from the right
for outer in range (len(myList)-1,0,-1):
  for inner in range(outer):
    #compare two adjacent values
    if myList[inner+1]>myList[inner]:
      #assign one of the values to a temp variable
      temp = myList[inner+1]
      #overwrite one of the values
      myList[inner+1] = myList[inner]
      #replace with the temp value
      myList[inner] = temp
      swaps = swaps + 1


print("Bubble sort complete")
print(myList)
print("There were "+str(swaps)+" swaps")
