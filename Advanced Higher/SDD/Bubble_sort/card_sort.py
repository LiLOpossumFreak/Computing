myList = ['4_ofClubs','queen_ofSpades','3_ofDiamonds','7_ofSpades','ace_ofClubs']
swaps = 0

#Sorts into ascending order
#start from the right
for outer in range (len(myList)-1,0,-1):
  for inner in range(outer):
    if len(myList[inner][0:'_']) > 1:
      #do some stuff ig?
      print()
    else: 
      #compare two adjacent values
      if int(myList[inner][0:1]) > int(myList[inner+1][0:'_']):
         #assign one of the values to a temp variable
        temp = myList[inner]
         #overwrite one of the values
        myList[inner] = myList[inner+1]
         #replace with the temp value
        myList[inner+1] = temp
        swaps = swaps + 1


print("Bubble sort complete")
print(myList)
print("There were "+str(swaps)+" swaps")