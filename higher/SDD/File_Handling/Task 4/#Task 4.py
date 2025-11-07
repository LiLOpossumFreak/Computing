#Task 4
names = ["John","Joan","Mark","Michael"]
birthMonths = ["June","September","December","March"]
ages = [23,35,23,8]

with open("names.txt","w") as wfile:
    for counter in range(0,len(names)):
        wfile.write(names[counter] + "," + birthMonths[counter] + "," + str(ages[counter]) + "\n")