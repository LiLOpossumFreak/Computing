#Assignment 2025
filename = "SDD/2025_Assignment/orders.txt"
writeFilename = "SDD/2025_Assignment/winningCustomer.txt"
#Setting up 1 order record
from dataclasses import dataclass
@dataclass
class order():  
    orderNum : str = 0
    date : str = ""
    email : str = ""
    option : str = ""
    cost : float = 0
    rating : int = 0


#-----------------Subroutines-----------------------------------------------------

def ReadIntoArray():
    #sets up an array of 505 orders records
    orders = [order() for index in range(505)]
    CurrentItems = []
    index = 0
    with open(filename,"r") as OrdersFile:
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
            orders[index].rating = int(CurrentItems[5])
            index = index + 1
            # read next line
            currentLine = OrdersFile.readline().strip('\n') 
    return orders


def FindPosition(orders):
    #initalising variables
    position = -1
    index = 0
    month = str(input("Enter the month you want to search for: "))
    while position == -1 and index < len(orders):
        #sets monthIndex to the month in the date at the specific index
        monthIndex = orders[index].date[3:6]
        #if the month entered is found in the array, and the rating is 5, the position is recorded and the subroutine ends
        if monthIndex == month and orders[index].rating == 5:
            position = index
        index = index + 1
    return position


def WriteCustomerDetails(orders, position):
    with open(writeFilename,"w") as winningCustomerFile:
        if position == -1:
            #Writes 'No winner' to winningCustomer.txt if there is no winning customer
            winningCustomerFile.write("No winner")
            print("No Winner")
        else:
            #Writes the winning order number, email and cost to winningCustomer.txt if there's a winning customer
            winningCustomerFile.write(orders[position].orderNum+","+orders[position].email+", "+str(orders[position].cost))
            print("yeswinner")
    pass


def countOption(orders,CurrentOption):
    #set counter to 0
    counter = 0
    #Searches orders and counts the number of orders which match the current option
    for index in range(len(orders)):
        if orders[index].option == CurrentOption:
            counter = counter + 1
    return counter


def DisplayOrders(orders):
    noDelivered = countOption(orders,"Delivery")
    noCollected = countOption(orders,"Collection")
    #Displays the number of orders delivered and the number of orders collected
    print("There were "+str(noDelivered)+" delivered, and there were "+str(noCollected)+" collected.")
    pass


#---------------------main program--------------------------------

orders = ReadIntoArray()
position = FindPosition(orders)
WriteCustomerDetails(orders, position)
DisplayOrders(orders)