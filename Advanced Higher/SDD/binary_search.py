#---------------------- Subroutines ----------------------------------------------
def initialise():
    searchlist = [10,15,25,26,60,90,100]
    print("Original list:",searchlist)
    return searchlist


def BinarySearch(searchlist,goal):
    found = False
    startpos = 0
    endpos = len(searchlist) -1


    print ("Endpos at beginning = ",endpos)

    comparisonCount = 0
    while (startpos <= endpos) and found == False:
        middle = (startpos+endpos)//2 
        if searchlist[middle] == goal:
            found = True
        elif searchlist[middle]<goal:
            startpos = middle + 1
        else:
            endpos = middle -1
        comparisonCount = comparisonCount + 1

    print("There were "+str(comparisonCount)+" comparisons made.")
    if found == True:
        return middle
    else:
        return -1


def displayResults(foundPosition):
    if foundPosition > 0:
        print("Match has been found at position "+str(foundPosition))
    else:
        print("element not found.")
    pass

#---------------------- Main Program ----------------------------------------------

values = initialise()


goal = int(input("Enter goal: "))
foundPosition = BinarySearch(values,goal)
displayResults(foundPosition)