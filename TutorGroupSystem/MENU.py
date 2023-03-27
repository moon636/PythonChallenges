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

IndexList = ["ForeName: ",
             "Surname: ",
             "Date of birth: ",
             "Home Address: ",
             "Home phone number: ",
             "Gender: ",
             "Tutor: ",
             "Email Address: "
             ]

def checklogin(Iuser,Ipass):
    global loggedin
    global admin
    loggedin = False
    admin = False
    if (Iuser == "admin") and (Ipass == "123"):
        loggedin = True
        admin = True
    elif (Iuser == "moderator") and (Ipass == "abc"):
        loggedin = True   

def loopLoginIfIncorrect():
    while not loggedin:
        print("\nIncorrect password please enter again")
        username = input("\nenter username: ")
        password = input("enter password: ")
        
        checklogin(username,password)
        
while True: # log in menu
    print("\nWelcome to the tutor management system!\n")
    
    username = input("enter username: ")
    password = input("enter password: ")
    
    checklogin(username,password)
    
    loopLoginIfIncorrect()

    while True: #menu once logged in
        
        print("""
1) Display all students data
2) Search for a student to view details
3) Delete student
4) Add a student
5) Report Menu
6) Log out""")
        
        UserInput = input("\nSelect a number choice from above: ")
        
        while True:
            if not UserInput.isnumeric():
                UserInput = input("\nThat is not a number! Enter a number: ")
            else:
                UserInput = int(UserInput)
                if (UserInput < 1) or (UserInput>6):
                    UserInput = input("\nThat is not a number from the menu! Enter a number from 1 to 6: ")
                else:
                    break

        if UserInput == 1:
            print("") #new line
            for key in data:
                print(key+" : ",end="")
                for value in data[key]:
                    print(value+", ",end="")
                print("") #new line
                
        elif UserInput == 2:
            UserInput = input("\nEnter the student ID to search for: ").upper()
            
            Found = 0
            
            for key in data.keys():
                if key == UserInput:
                    Found = True
                    StudentData = data[key]
                    index = 0
                    print("") #new line
                    printNicely("Student Id: "+key)
                    for i in StudentData: #printing user data nicely
                        printNicely(IndexList[index]+i)
                        index += 1

                    
            if not Found:
                print("\nThat student does not exist in the data")

        elif UserInput == 3:
            UserInput = input("\nEnter the student ID to search for: ").upper()
            
            Found = False
            index = None
            for key in data:
                if key == UserInput:
                    Found = True
                    index = key
                   
            if Found:
                del data[index]
                updatefile(data)
                print("\nThe student has been removed from the data")
            else:
                print("\nThat student does not exist in the data")

        elif UserInput == 4:
            StudentId = input("Enter the students ID: ")
            StudentForeName = input("Enter the students forename: ")
            StudentSurName = input("Enter the students surname: ")
            StudentDOB = input("Enter the students date of birth: ")
            StudentAddress = input("Enter the students Address: ")
            StudentHomePhoneNumber = input("Enter the students home phone number: ")
            StudentGender = input("Enter the students gender: ")
            StudentTutor = input("Enter the students Tutor: ")
            StudentEmail = input("Enter the students email address: ")

            data.update({StudentId:[StudentForeName,StudentSurName,StudentDOB,StudentAddress,StudentHomePhoneNumber,StudentGender,StudentTutor,StudentEmail]})
            updatefile(data)
        elif UserInput == 5:

            while True:
                print("""
1) Display all genders
2) Display all emails
3) Display all addresses
4) Return to main menu""")

                UserInput = input("\nSelect a number choice from above: ")

                while True:
                    if not UserInput.isnumeric():
                        UserInput = input("\nThat is not a number! Enter a number: ")
                    else:
                        UserInput = int(UserInput)
                        if (UserInput < 1) or (UserInput>4):
                            UserInput = input("\nThat is not a number from the menu! Enter a number from 1 to 4: ")
                        else:
                            break

                if UserInput == 1:
                    print("") #new line
                    for key in data:
                        print(data[key][5])
                elif UserInput == 2:
                    print("") #new line
                    for key in data:
                        print(data[key][7])
                elif UserInput == 3:
                    print("") #new line
                    for key in data:
                        print(data[key][3])
                    
                elif UserInput == 4:
                    break
                
        elif UserInput == 6:
            print("\nLogged Out")
            break #return to log in
        else:
            print("\nThat is not a valid option.")

    
