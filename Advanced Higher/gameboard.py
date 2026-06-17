from dataclasses import dataclass

@dataclass
class square():
    position : int = 0
    player : str = ''
    pointer : int = 0

gameboard = [square() for index in range(50)]

import random

#------------ Subroutines ---------------------

def InputPlayerColour(gameboard):
      gameboard[0].player = str(input("enter P1's colour - either red, blue, green or yellow: "))
      while gameboard[0].player != "red" and gameboard[0].player != "blue" and gameboard[0].player != "green" and gameboard[0].player != "yellow":
            print("ERROR YOU STUPID IDIOT INVALID COLOUR!!!!!!!!!! >:((")
            gameboard[0].player = str(input("enter P1's colour - either red, blue, green or yellow: "))
    
      index = 1
      for index in range(49):
            gameboard[index].player = "empty"
            index = index + 1
      return gameboard

def displayBoard(gameboard):
    for row in range(len(gameboard)):
        print(str(gameboard[row].position) + ', ',end='')
    print()


def initPosition(gameboard):
    for index in range(len(gameboard)):
        gameboard[index].position = index + 1
    return gameboard


def AssignPointer(gameboard):
    for index in range(len(gameboard)):
        if gameboard[index].position == 5:
            gameboard[index].pointer = 7

        elif gameboard[index].position == 12:
            gameboard[index].pointer = 9	

        elif gameboard[index].position == 16:
            gameboard[index].pointer = 19

        elif gameboard[index].position == 23:
            gameboard[index].pointer = 19
		
        elif gameboard[index].position == 27:
            gameboard[index].pointer = 28	

        elif gameboard[index].position == 32:
            gameboard[index].pointer = 36	

        elif gameboard[index].position == 36:
            gameboard[index].pointer = 31	

        elif gameboard[index].position == 45:
            gameboard[index].pointer = 47

        elif gameboard[index].position == 48:
            gameboard[index].pointer = 45		

        else:
            gameboard[index].pointer = 0
    return gameboard


def MOVE(gameboard):
    playerColour = gameboard[0].player
    SquaresToMove = random.randint(1,6)
    NewSquare = SquaresToMove
    while NewSquare < 50:
        for index in range(len(gameboard)):
            gameboard[index].player = 'empty'
        gameboard[NewSquare].player ==  playerColour
        SquaresToMove = random.randint(1,6)
        NewSquare = NewSquare + SquaresToMove
    return gameboard

#------------ Main Program -------------------------------------

gameboard = InputPlayerColour(gameboard)
gameboard = initPosition(gameboard)
displayBoard(gameboard)
gameboard = AssignPointer(gameboard)
gameboard = MOVE(gameboard)
