#Assignment 2025

#Setting up 1 order record
from dataclasses import dataclass
@dataclass
class order():
    orderNum : int = 0
    date : str = ""
    email : str = ""
    option : str = ""
    cost : int = 0
    rating : int = 0
#sets up an array of 505 orders records
orders = [order() for index in range(505)]


#Subroutines
def ReadIntoArray():
    index = 0
    with open("orders.txt","r") as OrdersFile:
        #reads the current line
        currentLine = OrdersFile.readline().strip('\n')
        #ensures the program will stop reading from the file once it reaches an empty line
        while currentLine != "":
            #splits the current line at every comma and saves each section as elements in the arry CurrentItems
            CurrentItems = currentLine.split(",")
            #saves each item in CurrentItems into a record
            orders[index].orderNum = CurrentItems[0]
            orders[index].date = CurrentItems[1]
            orders[index].email = CurrentItems[2]
            orders[index].option = CurrentItems[3]
            orders[index].cost = CurrentItems[4]
            orders[index].rating = CurrentItems[5]
            index = index + 1
    return orders

def FindPosition(orders):
    #initalising variables
    position = -1
    index = 0
    month = str(input("Enter the month you want to search for: "))
    while position == -1 and index < len(orders):
        #splits the date at the current index into multiple items in an array
        Date = orders[index].date.split("-")
        #sets monthIndex to the month for the current index
        monthIndex = Date[1]
        #if the month entered is found in the array, and the rating is 5, the position is recorded and the subroutine ends
        if monthIndex == month and orders[index].rating == 5:
            position = index
        index = index + 1
    return position

def WriteCustomerDetails(orders, position):
    with open("winningCustomer.txt","w") as winningCustomerFile:
        if position <= 0:
            winningCustomerFile.write()
        else:
            winningCustomerFile.write()
    pass

def DisplayOrders(orders):
    pass


#main program
orders = ReadIntoArray()
position = FindPosition(orders)
WriteCustomerDetails(orders, position)
DisplayOrders(orders)