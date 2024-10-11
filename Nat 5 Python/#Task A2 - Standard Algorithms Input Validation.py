#Task A2 - Standard Algorithms Input Validation

name = str(input("NAME PLEASE "))
age = int(input("AGE PLEASE "))
while age <11 or age >18 :
    age = int(input("ERROR AGE PLEASE "))

print("Hey there ",name," u got into talent show! Also ur ",age," years old loser")