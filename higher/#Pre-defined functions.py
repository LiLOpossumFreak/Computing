#Pre-defined functions

#Task 1
value = 0

password = input("Please enter your password: ")
chars = list(password)
for index in range(len(chars)):
    value = value + ord(chars[index])
remainder = value%11
NewPassword = str(remainder) + password
#print so I can see if the code is working
print(NewPassword)


#Task 2