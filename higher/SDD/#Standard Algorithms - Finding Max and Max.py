#Standard Algorithms - Finding Max and Min

#Task 3 
runner_name = ["AS","CM","ZN","OR","FP"]
runner_num = [2191,1789,1046,3391,2192]
runner_time = [49.18,51.36,42.58,58.59,64.03]
money_raised = [312.50,240.75,210.00,278.90,180.00]

def displayNumbers (numbers):
  for x in range(len(numbers)):
    print  (numbers[x]," ",end="")
  return

def findingMin (numbers):
  position = 0
  min = runner_time[0]
  for index in range(len(runner_time)):
    if min > runner_time[index]:
      min = runner_time[index]
  print()
  print("The lowest number (minimum) in the list is",min,".")
  return position

displayNumbers(runner_time)
position = findingMin(runner_time)
print("The runner who was fastest is:",runner_name[position])
print("Their runner number was",runner_num[position])
print("The amount raised for charity was",money_raised[position])


#Task 6
from random import *

numbers = []

def random20numbers():
  for x in range(20):
    numbers.append(randrange(1,51))
  return numbers

def displayNumbers (numbers):
  for x in range(20):
    print  (numbers[x]," ",end="")

def findingMax(numbers):
  max = numbers[0]
  for index in range(len(numbers)):
    if numbers[index] > max:
      max = numbers[index]
  print()
  print("The highest number (maximum) in the list is",max,".")

numbers = random20numbers()
displayNumbers(numbers)
findingMax(numbers)
