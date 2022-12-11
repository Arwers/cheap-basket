# prints out whats in the basket
def showBasket(groceries, args):
    # [name, amount, price]
    for i in range(len(groceries)):
        for j in range(len(args)):
            print(args[j] + ": " + groceries[i][j] + " ", end='')
        print("\n")

# return list on info about product, that will be added to the list
def addProduct(args):
    # empty list, can be usefull later
    product = [0,0,0]
    for i in range(len(args)):
        product[i] = input(args[i] + ": ") 
    return product

# searches for item in the groceries list, and returns it if exist
def removeProduct(groceries, name):
    # check every product
    for i in range(len(groceries)):
        # groceries[i][0] contains name of the product
        if(groceries[i][0] == name):
            return groceries[i]
    # in case product doesnt exist
    return "-1"

print(""" 
            GROCERY BASKET
    MENU:
    1 - open your list of groceries
    2 - add product from the list
    3 - remove product from the list
    0 - turn off
""")

# current action from the menu
action = 9
# list of groceries
groceries = []
# informations that we collect about product
args = ["name", "amount", "price"]

while(action != 0):
    # input type of operation
    action = int(input("Action: "))
    
    # show whats in the basket
    if(action == 1):
        showBasket(groceries, args)
    
    # add product
    elif(action == 2):
        groceries.append(addProduct(args))
    
    # if on the list, remove product
    elif(action == 3):
        temp = removeProduct(groceries, input("Name: "))
        if(temp == "-1"):
            print("Product is not on the list")
        else:
            groceries.remove(temp)
