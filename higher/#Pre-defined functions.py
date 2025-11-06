#Pre-defined functions

#Task 1
value = 0

password = input("Please enter your password: ")
characters = list(password)
for index in range(len(characters)):
    value = value + ord(characters[index])
remainder = value%11
NewPassword = str(remainder) + password
#print so I can see if the code is working
print(NewPassword)


print()

#Task 2
NewAnimal = ""

animal = str(input("Please enter an animal: "))
characters = list(animal)
characters[0] = str(characters[0]).upper()
for index in range(len(characters)):
    NewAnimal = NewAnimal + str(characters[index])
print(NewAnimal)


print()

#Task 3
password = input("Please enter your password: ")
chars = list(password)
while chars[0] != str(chars[0]).upper():
    password = str(input("FIRST CHARACTER MUST BE A CAPITAL. Please re-enter your password: "))
while ord(chars[len(chars)]) < 35 or ord(chars[len(chars)]) > 37:
    password = str(input("LAST CHARACTER MUST BE EITHER #, $ OR %. Please re-enter your password: "))
print(password)