#Revision

from dataclasses import dataclass
@dataclass
class student():
    name : str = ""
    YearGroup : str = ""
    examScore : int = 0

students= [student() for index in range(3)]

#Subroutines
def getStudents(students):
    for index in range(len(students)):
        students[index].name = str(input("name: "))
        students[index].YearGroup = str(input("year group: "))
        students[index].examScore = int(input("exam score: "))
    return students

def passingStudentsFile(students):
    for index in range(len(students)):
        with open("higher/SDD/passingStudents.txt","w") as writefile:
            if students[index].examScore > 50:
                writefile.write(students[index])

#Main
students = getStudents(students)
passingStudentsFile(students)