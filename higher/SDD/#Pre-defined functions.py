#Pre-defined functions

#Task 1
value = 0

password = input("Please enter your password: ")
characters = list(password)
for index in range(len(characters)):
    value = value + ord(characters[index])
remainder = value%11
NewPassword = password + str(remainder)
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
def isPasswordSecure():
    password = input("Please enter your password: ")
    chars = list(password)
    test1 = (ord(chars[len(chars)-1]) < 35 or ord(chars[len(chars)-1]) > 37) # true / false
    test2 = chars[0] != str(chars[0]).upper() # true / false
    print(test1, test2) # to show what the program is doing
    while test1 or test2:
        password = str(input("FIRST CHARACTER MUST BE A CAPITAL AND LAST MUST BE EITHER #, $ or %. Please re-enter your password: "))
        chars = list(password)
        test1 = (ord(chars[len(chars)-1]) < 35 or ord(chars[len(chars)-1]) > 37) # true / false
        test2 = chars[0] != str(chars[0]).upper() # true / false
        print(test1, test2)
    return password

# --------- Main Program ---------

password = isPasswordSecure()
print(password," is secure. Yay.")