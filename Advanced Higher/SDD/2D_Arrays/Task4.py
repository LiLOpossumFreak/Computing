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
	def getWinner(self):
		return self.winner
	def getWinningLine(self):
		return self.winningLine

winnerValuesNotArray = winnerValues()

#----------------- Subroutines ---------------------------------------------
 
# TODO 1: check rows
def checkRows(winnerValuesNotArray):
	for row in range(3):
		if board[row] == ['X', 'X', 'X']:
			winnerValuesNotArray.setWinner('X')
			winnerValuesNotArray.setWinningLine('row ' + str(row + 1))
		if board[row] == ['O', 'O', 'O']:
			winnerValuesNotArray.setWinner('O')
			winnerValuesNotArray.setWinningLine('row ' + str(row + 1))
	return winnerValuesNotArray


# TODO 2: check columns
def checkColumns(winnerValuesNotArray):
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
			winnerValuesNotArray.setWinningLine('column ' + str(index-1))
			#there has to be a better solution but this works
			#(previously printed: ['X'] has won when set winner to currentColumn[0])
			if currentColumn[0] == ['X']:
				winnerValuesNotArray.setWinner('X')
			else:
				winnerValuesNotArray.setWinner('O')
	return winnerValuesNotArray


# TODO 3: check diagonals
def checkDiagonals(winnerValuesNotArray):
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
				winnerValuesNotArray.setWinner('X')
				winnerValuesNotArray.setWinningLine('a diagonal')
			else:
				winnerValuesNotArray.setWinner('O')
	return winnerValuesNotArray


# TODO 4: report the result
def displayResult(winnerValuesNotArray):
	if winnerValuesNotArray.getWinner != '':
		print(winnerValuesNotArray.getWinner(), 'has won')
		print('The win occured at',winnerValuesNotArray.getWinningLine())
	else:
		print('No winner')
	pass

#------- Main Program -----------------------------------------------

winnerValuesNotArray = checkRows(winnerValuesNotArray)
winnerValuesNotArray = checkColumns(winnerValuesNotArray)
winnerValuesNotArray = checkDiagonals(winnerValuesNotArray)
displayResult(winnerValuesNotArray)