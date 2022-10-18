def readfile():
    with open('stockdata.txt', 'r') as file:
        return file.read()

def appendfile(text):
    with open('stockdata.txt', 'a') as file:
        file.write(text)

def updatefile(filedata):
    with open('stockdata.txt', 'w') as file:
        file.write(str(filedata))

def pll(amount): #printing long lines so the menu looks cleaner
    print("-"*amount)

appendfile("") # creates a file if there isnt one already, if there is one it does nothing

data = {}

try:
    data = eval(readfile())
except:
    data = {}

def addproduct(pid,name,dep,loc,quantity,priceEVT):
    data.update({pid : [name,dep,loc,quantity,priceEVT,priceEVT * 1.2]})
    updatefile(data)

def removeproduct(pid):
    del data[pid]
    updatefile(data)

def removestock(pid,amount):
    data[pid][3] -= amount
    updatefile(data)
    
def addstock(pid,amount):
    data[pid][3] += amount
    updatefile(data)


def ReturnProductFromName(name):
    for item in data.values():
        if item[0] == name:
            return item
    
while True:
    print("\n")
    print("1. Search for product")
    print("2. Add product")
    print("3. Remove product")
    print("4. Add stock")
    print("5. Remove stock")
    print("\n")
    
    inp = input("Choose an option from above, enter 1 to 5: ")
    
    if inp == "1":
        print("\nSearch by:\n1. Product Id\n2. Product Name")
        search_type = input("\nEnter 1/2 based on the options above: ")
        if search_type == "1":
            searchid = input("\nEnter product id to search for: ")
            print("\nLocation: "+str(data[searchid])[2]+"\nQuantity: "+str(data[searchid][3]))
        if search_type == "2":
            searchname = input("\nEnter product name to search for: ")
            item = ReturnProductFromName(searchname)
            print("\nLocation: "+str(item[2])+"\nQuantity: "+str(item[3]))
    if inp == "2":
        pid = input("\nEnter product id: ")
        name = input("Enter product name: ")
        dep = input("Enter department: ")
        loc = input("Enter location: ")
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter price: "))

        addproduct(pid,name,dep,loc,quantity,price)
        print(data)
    if inp == "3":
        print("\Remove by:\n1. Product Id\n2. Product Name")
        search_type = input("\nEnter 1/2 based on the options above: ")
        if search_type == "1":
            searchid = input("\nEnter product id to search for: ")
            del data[searchid]
        if search_type == "2":
            searchname = input("\nEnter product name to search for: ")
            item = ReturnProductFromName(searchname)
            del item
    if inp == "4":
        pid = input("\nEnter product id: ")
        adds = int(input("Enter amount to add to the stock: "))
        addstock(pid,adds)
    if inp == "5":
        pid = input("\nEnter product id: ")
        removes = int(input("Enter amount to remove from the stock: "))
        removestock(pid,removes)        
        
