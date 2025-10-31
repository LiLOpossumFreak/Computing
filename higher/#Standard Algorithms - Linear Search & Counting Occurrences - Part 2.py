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
        found = True
    i = i + 1

  return foundPosition

#. *************MAIN*************

target = getTargetCharacter()
characters = getCharacters()
foundPosition = findCharacterPosition(target)
print(target," was found at position ",foundPosition)