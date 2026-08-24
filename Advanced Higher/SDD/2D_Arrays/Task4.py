board = [
	['X', 'X', 'X'],
	['O', 'X', 'O'],
	['O', 'O', 'X']
]
 
for row in range(3):
	print(board[row])
 
winner = ''
 
# TODO 1: check rows
for row in range(3):
	if board[row] == ['X', 'X', 'X']:
		winner = 'X'
	if board[row] == ['O', 'O', 'O']:
		winner = 'O'

# TODO 2: check columns
	

# TODO 3: check diagonals
 
# TODO 4: report the result
if winner == '':
	print('No winner')
else:
    print(winner, 'has won')
