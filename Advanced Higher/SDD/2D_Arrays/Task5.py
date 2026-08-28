seat = [ ['' for col in range(5)] for row in range(2)]
seat[0][0] = 'D'
seat[0][1] = 'AB'
seat[0][2] = 'MD'
seat[1][4] = 'LL'
seat[1][0] = 'ES'
seat[1][2] = 'T'


for row in range(2):
    print(seat[row])


class userDetails:
	def _init_(self):
		self.initals = ''
		self.row = 0
		self.column = 0
	#setters
	def setInitals(self, initals):
		self.initals = initals
	def setRow(self, row):
		self.row = row
	def setColumn(self, column):
		self.column = column
	#getters
	def getInitals(self):
		return self.initals
	def getRow(self):
		return self.row
	def getColumn(self):
		return self.column

userDetailsVariable = userDetails()

#------------------ subroutines ----------------------------------

# TODO 1: ask the user for their initials, and a row and column for their seat
def getDetailsFromUser(userDetailsVariable):
	userDetailsVariable.setInitals(input("Please input your initals: "))
	userDetailsVariable.setRow(input("Please input your row: "))
	userDetailsVariable.setColumn(input("Please input your column: "))
	return userDetailsVariable

# TODO 2: check whether that row and column is free (equal to '')
def checkSeats():
	pass

# TODO 3: if it is free, store the initials at that row and column


# TODO 4: if it is not free, display an error message and ask again for a row and column

#----------------- main program ----------------------------------

userDetailsVariable = getDetailsFromUser(userDetailsVariable)
userDetailsVariable = checkSeats(userDetailsVariable)