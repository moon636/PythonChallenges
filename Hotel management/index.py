def readfile():
    with open('data.txt', 'r') as file:
        return file.read()

def appendfile(text):
    with open('data.txt', 'a') as file:
        file.write(text)

def updatefile(filedata):
    with open('data.txt', 'w') as file:
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


while True:

    print("""
1) Hotel Management Menu
2) Customer Menu
""")
    
    UserInput = input("\nSelect a number choice from above: ")

    while True:
        if not UserInput.isnumeric():
            UserInput = input("\nThat is not a number! Enter a number: ")
        else:
            UserInput = int(UserInput)
            if (UserInput < 1) or (UserInput>2):
                UserInput = input("\nThat is not a number from the menu! Enter a number 1 or 2: ")
            else:
                 break

    while True:
        if UserInput == 1: #hotel management menu
            
            print("""
1) Delete a booking
""")
            
            UserInput = input("\nSelect a number choice from above: ")
            
            while True:
                if not UserInput.isnumeric():
                    UserInput = input("\nThat is not a number! Enter a number: ")
                else:
                    UserInput = int(UserInput)
                    if (UserInput < 1) or (UserInput>1):
                        UserInput = input("\nThat is not a number from the menu! Enter a number from there: ")
                    else:
                        break
                
            if UserInput == 1:
                CustomerName = input("Enter room holder's name: ")

                Found = False
                index = None
                
                for key in data:
                    print(key)
                    print(data[key])
                    if key == CustomerName:
                        Found = True
                        index = key

                if Found:
                    del data[index]
                    updatefile(data)
                    print("\nThe booking has been removed from the data")
                else:
                    print("\nThat booking does not exist in the data")

            
            break
        else: #customer menu

            print("""
1) Book a room""")
            
            UserInput = input("\nSelect a number choice from above: ")
            
            while True:
                if not UserInput.isnumeric():
                    UserInput = input("\nThat is not a number! Enter a number: ")
                else:
                    UserInput = int(UserInput)
                    if (UserInput < 1) or (UserInput>1):
                        UserInput = input("\nThat is not a number from the menu! Enter a number from there: ")
                    else:
                        break
                
            if UserInput == 1:
                CustomerName = input("Enter your name: ")
                CustomerRoomType = input("Enter what type of room you want (basic/standard/premium): ")
                CustomerPeopleAmount = input("How many people are you booking this room for: ")
                CustomerDays = input("How many days will you be staying: ")

                data.update({CustomerName:[CustomerRoomType,CustomerPeopleAmount,CustomerDays]})
                updatefile(data)

            
