myList = ['G','X','b','P','z']
swaps = 0

#Sorts into ascending order
#start from the right
for outer in range (len(myList)-1,0,-1):
  for inner in range(outer):
    #compare two adjacent values
    if ord(myList[inner]) > ord(myList[inner+1]):
      #assign one of the values to a temp variable
      temp = ord(myList[inner])
      #overwrite one of the values
      ord(myList[inner]) == ord(myList[inner+1])
      #replace with the temp value
      ord(myList[inner+1]) == temp
      swaps = swaps + 1


print("Bubble sort complete")
print(myList)
print("There were "+str(swaps)+" swaps")