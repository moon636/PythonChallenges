def readfile():
    with open('userdata.txt', 'r') as file:
        return file.read()

def appendfile(text):
    with open('userdata.txt', 'a') as file:
        file.write(text)

def updatefile(filedata):
    with open('userdata.txt', 'w') as file:
        file.write(str(filedata))

def printNicely(toprint): #looks cleaner
        print("-"*len(toprint)) #printing a line with the length of the string
        print(toprint)
        print("-"*len(toprint))

appendfile("") # creates a file if there isnt one already, if there is one it does nothing

data = {}

try:
    data = eval(readfile())
except:
    data = {} #if there isnt any data then make a blank dictionary


while True: # loop the system
    print("\n")
    print("1. Search for user")
    print("2. Add user")
    print("3. Remove user")
    print("4. Update user's high score")
    print("\n")
    
    inp = input("Choose an option from above, enter 1 to 4: ")
    
    if inp == "1":
        searchname = input("\nEnter user's name to search for: ")
        if searchname in data:
            print("\n")
            printNicely("User: "+searchname+"\nHigh Score: "+data[searchname])
        else:
            print("\n")
            printNicely("User: "+searchname+" does not exist in the data")
            
    elif inp == "2":
        name = input("Enter user's name: ")
        if name in data:
            print("\n")
            printNicely("User: "+name+" already exists in the data")
            
        else:
            highScore = input("\nEnter user's high score: ")
            
            data.update({name : highScore})
            updatefile(data)
            
            print("\n")
            printNicely(name+" has been added with the high score of "+highScore)
            
    elif inp == "3":
        
        searchname = input("\nEnter user's name to delete: ")
        
        if searchname in data:
            del data[searchname]
            updatefile(data)
            
            print("\n")
            printNicely("User: "+searchname+" has been removed from the data")
            
            
        else:
            print("\n")
            printNicely("User: "+searchname+" does not exist in the data")

    elif inp == "4":
        
        searchname = input("\nEnter user's name to update high score: ")
        
        if searchname in data:
            highScore = input("\nEnter user's new high score: ")
            
            data.update({searchname : highScore})
            updatefile(data)
            
            print("\n")
            printNicely(searchname+" has been updated with the high score of "+highScore)
            
            
        else:
            print("\n")
            printNicely("User: "+searchname+" does not exist in the data")
            
    else:
        print("\n") 
        printNicely("Thats not an option!")
        
