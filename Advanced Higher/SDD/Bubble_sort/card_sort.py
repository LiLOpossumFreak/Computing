myList = ['4_ofClubs','Q_ofSpades','3_ofDiamonds','7_ofSpades','A_ofClubs']
swaps = 0

#Sorts into ascending order
#start from the right
for outer in range (len(myList)-1,0,-1):
  for inner in range(outer):
    #checks whether starting character is a number or letter
    if ord(myList[inner][0:1]) > 58:
      print('hello world')
  
    else: 
      #compare two adjacent integer values
      if int(myList[inner][0:1]) > int(myList[inner+1][0:1]):
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