myList = ['p','o','r','t','y']
swaps = 0

#sorts into ascending order
for index in range (1,len(myList)):
#store the value to be inserted into the array
    currentvalue = myList[index]
    position = index

  #shift the rest of the array one to the right
    while position > 0 and ord(myList[position-1]) > ord(currentvalue):
        myList[position] = myList[position-1]
        position -= 1

 #insert the value into the array
    myList[position] = currentvalue
    
    swaps =  swaps + 1


print(myList)
print(swaps)