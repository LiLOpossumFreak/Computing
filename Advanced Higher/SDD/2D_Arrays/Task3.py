rows = 4
cols = 6
seats = [['' for c in range(cols)] for r in range(rows)]
 
# TODO 1: fill every seat with '-'
seats[x][y] = '-'

# TODO 3: mark seats (1,1), (2,4) and (3,0) as 'X'


# TODO 2: display the grid neatly, one row per line
for row in range(rows):
	print(seats[row])
 
# TODO 4: count and display the number of free seats
