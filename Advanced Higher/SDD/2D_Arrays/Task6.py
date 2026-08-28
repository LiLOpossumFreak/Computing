students = ['Ali', 'Bea', 'Cal', 'Dee', 'Eve']
marks = [
	[14, 16, 12, 18],
	[9,  11, 15, 10],
	[20, 19, 18, 20],
	[7,  8,  10, 6],
	[15, 14, 16, 17]
]
 
for r in range(len(marks)):
	print(students[r], marks[r])
print()
 
# TODO 1: average mark per student
def avgMarksPerStudent(marks, students):
	for student in range(len(students)):
		average = 0
		for index in range(len(marks[0])):
			average = average + marks[student][index]
		average = round(average/len(marks[0]))
		print(students[student]+' gets an average of '+str(average)+' marks per test')
	pass

# TODO 2: average mark per test (per column)
def avgMarksPerTest(marks, students):
	for student in range(len(marks[0])):
		average = 0
		for index in range(len(students)):
			average = average + marks[student][index]
		average = round(average/len(students))
		print('There was an average of '+average+' marks for this test')
	pass

# TODO 3: highest mark, student and test
def highestMark(marks, students):
	pass

# TODO 4: lowest mark, student and test
def lowestMark(marks, students):
	pass

#---------------- main program --------------------------------------------

avgMarksPerStudent(marks, students)
print()
avgMarksPerTest(marks, students)
print()
highestMark(marks, students)
print()
lowestMark(marks, students)