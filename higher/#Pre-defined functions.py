#Pre-defined functions

#Task 1
password = input("Please enter your password: ")
chars = list(password)
for index in range(len(chars)):
    remainder = ord(chars[index]) - ord(chars[index])%11
NewPassword = remainder + password
print(NewPassword)