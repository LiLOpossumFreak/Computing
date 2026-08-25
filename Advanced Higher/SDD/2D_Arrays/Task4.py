board = [
	['X', 'X', 'X'],
	['O', 'O', 'O'],
	['O', 'O', 'X']
]
 
for row in range(3):
	print(board[row])
print()
 
winner = ''
winningLine = []
 
# TODO 1: check rows
for row in range(3):
	if board[row] == ['X', 'X', 'X']:
		winner = 'X'
		winningLine = 'row ' + str(row)
	if board[row] == ['O', 'O', 'O']:
		winner = 'O'
		winningLine = 'row ' + str(row)


# TODO 2: check columns
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
		winningLine = 'column ' + str(index-1)
		#there has to be a better solution but this works
		#(previously printed: ['X'] has won when set winner to currentColumn[0])
		if currentColumn[0] == ['X']:
			winner = 'X'
		else:
			winner = 'O'


# TODO 3: check diagonals
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
			winner = 'X'
			winningLine = 'a diagonal'
		else:
			winner = 'O'


# TODO 4: report the result
if winner != '':
	print(winner, 'has won')
	print('The win occured at',winningLine)
else:
	print('No winner')