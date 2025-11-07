#Standard Algorithms - Linear Search & Counting Occurrences - Part 2


#Task 3
def getTargetCharacter():
  target = input("Enter the character you are looking for :")

  return target

def getCharacters():
  characters = ["Desperate Dan", "Numbskulls", "Dennis the Menace", "Minnie the Minx", "Walter", "Gnasher", "Billy Whizz"]

  return characters

def findCharacterPosition(oneToFind):
  found = False
  foundPosition = -1
  i = 0
  while found == False and i < len(characters):
    foundPosition = foundPosition + 1
    if characters[i] == target:
        found == True
    i = i + 1

  return foundPosition, found

#. *************MAIN*************

characters = getCharacters()
target = getTargetCharacter()
foundPosition, found = findCharacterPosition(target)
if found == True:
  print(target," was found at position ",foundPosition)
else:
  print(target," was not found :(")





#Task 4
def getTarget():
  targetAnimal = input("Please enter the target animal you are searching for: ")

  return targetAnimal

def getCircusAnimalsList():
  animals = ["giraffe", "chicken", "lion", "cheetah", "rat", "elephant", "snake", "chicken", "horse"]

  return animals

def countOccurrences(targetAnimal, animals):
  occurrences = 0
  for index in range(len(animals)):
    if animals[index] == targetAnimal:
      occurrences = occurrences + 1
  return occurrences


#*************  MAIN *************

targetAnimal = getTarget()
animals= getCircusAnimalsList()
occurrences = countOccurrences(targetAnimal, animals)
print("There were ",occurrences," of ",targetAnimal)