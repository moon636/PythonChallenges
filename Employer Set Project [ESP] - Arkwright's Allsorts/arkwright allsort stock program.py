import aasModule

data = {}
try:
    data = eval(aasModule.readfile())
except:
    data = {}

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
            item = aasModule.ReturnProductFromName(searchname)
            print("\nLocation: "+str(item[2])+"\nQuantity: "+str(item[3]))
    if inp == "2":
        pid = input("\nEnter product id: ")
        name = input("Enter product name: ")
        dep = input("Enter department: ")
        loc = input("Enter location: ")
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter price: "))

        aasModule.addproduct(pid,name,dep,loc,quantity,price)
        print(data)
    if inp == "3":
        print("\Remove by:\n1. Product Id\n2. Product Name")
        search_type = input("\nEnter 1/2 based on the options above: ")
        if search_type == "1":
            searchid = input("\nEnter product id to search for: ")
            del data[searchid]
        if search_type == "2":
            searchname = input("\nEnter product name to search for: ")
            item = aasModule.ReturnProductFromName(searchname)
            del item
    if inp == "4":
        pid = input("\nEnter product id: ")
        adds = int(input("Enter amount to add to the stock: "))
        aasModule.addstock(pid,adds)
    if inp == "5":
        pid = input("\nEnter product id: ")
        removes = int(input("Enter amount to remove from the stock: "))
        aasModule.removestock(pid,removes)        
        
