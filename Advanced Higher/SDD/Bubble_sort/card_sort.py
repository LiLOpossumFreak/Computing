myList = ['4_ofClubs','Q_ofSpades','3_ofDiamonds','7_ofSpades','A_ofClubs']
swaps = 0

#Sorts into ascending order
#start from the right
for outer in range (len(myList)-1,0,-1):
  for inner in range(outer):
    #checks whether starting character is a number or letter
    if ord(myList[inner+1][0:1]) > 40:
      valueHold = myList[inner+1]
      #this is probably super inefficient but idk how to do it better and this is already late :(
      if myList[inner+1][0:1] == 'A':
          myList[inner+1] = 0
      elif myList[inner+1][0:1] == 'J':
        myList[inner+1] = 10
      elif myList[inner+1][0:1] == 'Q':
        myList[inner+1] = 11
      elif myList[inner+1][0:1] == 'K':
        myList[inner+1] = 12
  
    #compare two adjacent integer values
    if int(myList[inner][0:2].rstrip('_')) > int(myList[inner+1][0:2].rstrip('_')):
      #assign one of the values to a temp variable
      temp = myList[inner]
      #overwrite one of the values
      myList[inner] = myList[inner+1]
      #replace with the temp value
      if len(myList[inner]) > 2:
        myList[inner+1] = temp
      else:
        myList[inner+1] = valueHold
      swaps = swaps + 1

print("Bubble sort complete")
print(myList)
print("There were "+str(swaps)+" swaps")