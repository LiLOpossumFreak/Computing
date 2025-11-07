#803 Task 3 - Subroutines and Parameter Passing

blue = 6
red = 9
monday = 100

def module2(monday):
  monday = monday/10
  return monday

def module3(blue, red):
  total = 0
  for counter in range(blue, red):
    total = total + 2
    print(total)
    return total
  
print(module2(monday) + module3(blue, red))
