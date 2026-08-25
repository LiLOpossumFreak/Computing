board = [
	['X', 'X', 'X'],
	['O', 'O', 'O'],
	['O', 'O', 'X']
]
 
for row in range(3):
	print(board[row])
print()

class winnerValues:
	def _init_(self):
		self.winner = ''
		self.winningLine = ''
	#setters
	def setWinner(self, winner):
		self.winner = winner
	def setWinningLine(self, winningLine):
		self.winningLine = winningLine
	#getters
	def getWinner(self, winner):
		return self.winner
	def getWinningLine(self, winningLine):
		return self.winningLine

winnerValuesArray = [winnerValues() for index in range(1)]

#----------------- Subroutines ---------------------------------------------
 
# TODO 1: check rows
def checkRows(winnerValuesArray):
	for row in range(3):
		if board[row] == ['X', 'X', 'X']:
			winnerValuesArray[0].setWinner('X')
			winnerValuesArray[0].setWinningLine('row ' + str(row))
		if board[row] == ['O', 'O', 'O']:
			winnerValuesArray[0].setWinner('O')
			winnerValuesArray[0].setWinningLine('row ' + str(row))
	return winnerValuesArray


# TODO 2: check columns
def checkColumns(winnerValuesArray):
	s = 0
	l = 1
	for rows in range(3):
		currentColumn = []
		index = 0
		for cols in range(3):
			currentColumn.append(board[index][s:l])
			index = index + 1
		s = s + 1
		l = l + 1
		if currentColumn[0] == currentColumn[1] == currentColumn[2]:
			winnerValuesArray[0].setWinningLine('column ' + str(index-1))
			#there has to be a better solution but this works
			#(previously printed: ['X'] has won when set winner to currentColumn[0])
			if currentColumn[0] == ['X']:
				winnerValuesArray[0].setWinner('X')
			else:
				winnerValuesArray[0].setWinner('O')
	return winnerValuesArray


# TODO 3: check diagonals
def checkDiagonals(winnerValuesArray):
	s = 0
	b = 1
	for diagonals in range(2):
		currentDiagonal = []
		index = 0
		for squares in range(3):
			currentDiagonal.append(board[index][s:b])
			if diagonals == 0 and index < 2:
				s = s + 1
				b = b + 1
			elif diagonals == 1:
				s = s - 1
				b = b - 1
			index = index + 1
		if currentDiagonal[0] == currentDiagonal[1] == currentDiagonal[2]:
			if currentDiagonal[0] == ['X']:
				winnerValuesArray[0].setWinner('X')
				winnerValuesArray[0].setWinningLine('a diagonal')
			else:
				winnerValuesArray[0].setWinner('O')
	return winnerValuesArray


# TODO 4: report the result
def displayResult(winnerValuesArray):
	if winner != '':
		print(winner, 'has won')
		print('The win occured at',winningLine)
	else:
		print('No winner')
	return winnerValuesArray

#------- Main Program -----------------------------------------------

winnerValuesArray = checkRows(winnerValuesArray)
winnerValuesArray = checkColumns(winnerValuesArray)
winnerValuesArray = checkDiagonals(winnerValuesArray)
winnerValuesArray = displayResult(winnerValuesArray)