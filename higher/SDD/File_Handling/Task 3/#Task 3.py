#Task 3

items = []
names = []
marks = []

with open("higher/SDD/File_Handling/Task 3/pupils.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        names.append(items[0])
        marks.append(items[1])
        line = readfile.readline().rstrip('\n')

for index in range(len(names)):
    print(names[index],"-",marks[index],)
