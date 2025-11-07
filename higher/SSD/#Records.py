# 801. Records and Array of Records
# Example 2 - An array of records - Predict and Read

from dataclasses import dataclass
@dataclass
class person():
    height : float = 0.0
    weight : float = 0.0
    bmi : float = 0.0

BMIdetails = [person() for index in range(40)] # DECLARE BMIDetails(40) AS PERSON

for index in range(5):  
    BMIdetails[index].height  = float(input("Please input your height: "))
    BMIdetails[index].weight  = float(input("Please input your weight: "))
    BMIdetails[index].bmi = BMIdetails[index].weight / (BMIdetails[index].height ** 2
