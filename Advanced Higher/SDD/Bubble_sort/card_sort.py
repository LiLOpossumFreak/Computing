myList = ['4_ofClubs','Q_ofSpades','3_ofDiamonds','7_ofSpades','A_ofClubs']
swaps = 0

# sanitise data
for x in range(len(myList)):
  if ord(myList[x][0:1]) > 40:
        valueHold = myList[x]
        #this is probably super inefficient but idk how to do it better and this is already late :(
        if myList[x][0:1] == 'A':
            myList[x] = '0_' + myList[x][2:]
        elif myList[x][0:1] == 'J':
          myList[x] = '10_' + myList[x][2:]
        elif myList[x][0:1] == 'Q':
          myList[x] = '11_' + myList[x][2:]
        elif myList[x][0:1] == 'K':
          myList[x] = '12_' + myList[x][2:]

#Sorts into ascending order
#start from the right
for outer in range (len(myList)-1,0,-1):
  for inner in range(outer):  
    #compare two adjacent integer values
    if int(myList[inner][0:2].rstrip('_')) > int(myList[inner+1][0:2].rstrip('_')):
      #assign one of the values to a temp variable
      temp = myList[inner]
      #overwrite one of the values
      myList[inner] = myList[inner+1]
      #replace with the temp value
      if len(myList[inner+1]) > 2:
        myList[inner+1] = temp
      else:
        myList[inner+1] = valueHold
      swaps = swaps + 1

print("Bubble sort complete")
print(myList)
print("There were "+str(swaps)+" swaps")