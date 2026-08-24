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
for cols in range(3):
	currentColumn = []
	index = 0
	for x in range(3):
		currentColumn.append(board[index][s:l])
		index = index + 1
	s = s + 1
	l = l + 1
	#if currentColumn[0] == currentColumn[1] == currentColumn[2]:
		#winner = currentColumn[0]
	print(currentColumn[0])

# TODO 3: check diagonals
 
# TODO 4: report the result
if winner == '':
	print('No winner')
else:
    print(winner, 'has won')
