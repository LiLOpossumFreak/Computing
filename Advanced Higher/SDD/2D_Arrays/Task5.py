seat = [ ['' for col in range(5)] for row in range(2)]
seat[0][0] = 'D'
seat[0][1] = 'AB'
seat[0][2] = 'MD'
seat[1][4] = 'LL'
seat[1][0] = 'ES'
seat[1][2] = 'T'


for row in range(2):
    print(seat[row])

#------------------ subroutines ----------------------------------

# TODO 1: ask the user for their initials, and a row and column for their seat
def getDetailsFromUser():
    pass

# TODO 2: check whether that row and column is free (equal to '')


# TODO 3: if it is free, store the initials at that row and column


# TODO 4: if it is not free, display an error message and ask again for a row and column

#----------------- main program ----------------------------------

getDetailsFromUser()