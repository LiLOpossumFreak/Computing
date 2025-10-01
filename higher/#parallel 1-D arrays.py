#parallel 1-D arrays

# Write a program that will ask the user for their name and a test mark out of 100.
# This should be looped five times and the names and marks should be stored in separate arrays.
# Print out the contents of the names and the marks arrays. 

#initialise arrays
name = []
test_mark = []

#subroutines
def get_name():
    CurrentName = input("Enter your name: ")
    return CurrentName

def get_test_mark():
    CurrentMark = int(input("Enter your mark: "))
    while CurrentMark < 1 or CurrentMark > 100:
        print("ERROR!!!!!!!!!!!!!")
        CurrentMark = int(input("Enter your mark: "))
    return CurrentMark

def display_all(name,test_mark):
    for index in range(5):
        print(name[index] + " scored " + str(test_mark[index]))


#get array items
for index in range(5):
    name.append(get_name())
    test_mark.append(get_test_mark())
display_all(name,test_mark)
