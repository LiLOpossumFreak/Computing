rows = 4
cols = 6
seats = [['' for c in range(cols)] for r in range(rows)]
 
# TODO 1: fill every seat with '-'
for x in range(rows):
	for y in range(cols):
		seats[x][y] = '-'

# TODO 3: mark seats (1,1), (2,4) and (3,0) as 'X'
for x in range(rows):
	for y in range(cols):
		if x == 1 and y == 1:
			seats[x][y] = 'X'
		if x == 2 and y == 4:
			seats[x][y] = 'X'
		if x == 3 and y == 0:
			seats[x][y] = 'X'

# TODO 2: display the grid neatly, one row per line
row = ''
for x in range(rows):
	row = ''
	for y in range(cols):
		row += str(seats[x][y]) + ' , '
	row = row[:-2] 
	print(row)

# TODO 4: count and display the number of free seats
counter = 0
for x in range(rows):
	for y in range(cols):
		if seats[x][y] == '-':
			counter = counter + 1
print('There are ',counter,' seats available.')