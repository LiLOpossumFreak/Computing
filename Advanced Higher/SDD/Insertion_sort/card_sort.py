myList = ['4_ofClubs','Q_ofSpades','3_ofDiamonds','7_ofSpades','A_ofClubs']
swaps = 0


# sanitise data
for x in range(len(myList)):
  if ord(myList[x][0:1]) > 40:
        #this is probably super inefficient but idk how to do it better and this is already late :(
        if myList[x][0:1] == 'A':
            myList[x] = '0_' + myList[x][2:]
        elif myList[x][0:1] == 'J':
          myList[x] = '10_' + myList[x][2:]
        elif myList[x][0:1] == 'Q':
          myList[x] = '11_' + myList[x][2:]
        elif myList[x][0:1] == 'K':
          myList[x] = '12_' + myList[x][2:]


#sorts into descending order
for index in range (1,len(myList)):
#store the value to be inserted into the array
    currentvalue = int(myList[index][0:2].rstrip('_'))
    position = index

  #shift the rest of the array one to the right
    while int(myList[position][0:2].rstrip('_')) > 0 and int(myList[position-1][0:2].rstrip('_')) > currentvalue:
        myList[position] = myList[position-1]
        position -= 1

 #insert the value into the array
    myList[position] = currentvalue
    
    swaps =  swaps + 1


print(myList)
print('There were '+swaps+' swaps')