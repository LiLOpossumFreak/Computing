board = [
	['X', 'X', 'X'],
	['O', 'X', 'O'],
	['O', 'O', 'X']
]
 
for row in range(3):
	print(board[row])
print()
 
winner = ''

 
# TODO 1: check rows
for row in range(3):
	if board[row] == ['X', 'X', 'X']:
		winner = 'X'
	if board[row] == ['O', 'O', 'O']:
		winner = 'O'


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
		#there has to be a better solution but this works
		#(previously printed: ['X'] has won when set winner to currentColumn[0])
		if currentColumn[0] == ['X']:
			winner = 'X'
		else:
			winner = 'O'


# TODO 3: check diagonals
for diagonals in range(2):
	s = 0
	l = 1
	currentDiagonal = []
	for rows in range(3):
		index = 0
		for cols in range(3):
			currentDiagonal.append(board[index][s:l])
			index = index + 1
			#need to change s & l so that it does diagonals instead of columns
			s = s + 1
			l = l + 1
		if currentDiagonal[0] == currentDiagonal[1] == currentDiagonal[2]:
			#there has to be a better solution but this works
			#(previously printed: ['X'] has won when set winner to currentColumn[0])
			if currentDiagonal[0] == ['X']:
				winner = 'X'
			else:
				winner = 'O'


# TODO 4: report the result
if winner == '':
	print('No winner')
else:
    print(winner, 'has won')
