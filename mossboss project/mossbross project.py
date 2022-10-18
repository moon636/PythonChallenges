# The data will save in the file for the next time you use the program

def returnLgrade(num):
    if num<=40:
        return "Fail"
    elif num<=50:
        return "D"
    elif num<=60:
        return "C"
    elif num<=70:
        return "B"
    elif num<=80:
        return "A"
    elif num<=100:
        return "A*"
    else:
        return "score error"

    
def readfile():
    with open('StudentsTestData.txt', 'r') as file:
        return file.read()

def appendfile(text):
    with open('StudentsTestData.txt', 'a') as file:
        file.write(text)

def updatefile(filedata):
    with open('StudentsTestData.txt', 'w') as file:
        file.write(str(filedata))

def pll(amount): #printing long lines so the menu looks cleaner
    print("-"*amount)
    
appendfile("") # creates a file if there isnt one already, if there is one it does nothing

data = {}
try:
    data = eval(readfile())
except:
    data = {}
        
while True:
    print("\n")
    print("1. View all student test data")
    print("2. Add a student's test data")
    print("3. Remove student or test data")
    print("4. Exit menu")
    print("\n")

    inp = input("Select an option from 1-4 based on the menu above: ")
    print("\n")
    
    if inp == "1":
        print(data)
    elif inp == "2":
        name = input("What is the name of the student to add the test to: ")
        test = input("What is the name of the test to add to the student: ")
        score = int(input("What is the number score of the test for the student between 0-100: "))
        if name != "" and test != "" and score<= 100 and score >= 0: # checks
            newscore = returnLgrade(score)
            try:
                data[name].update({test : newscore})
                updatefile(data)
                te = test+" has been added to "+name+"'s test data table with the score of grade "+newscore
                print("\n")
                pll(len(te))
                print(te)
                pll(len(te))
            except:
                data.update({name : {test : newscore}})
                updatefile(data)
                te = test+" has been added to "+name+"'s test data table with the score of grade "+newscore
                print("\n")
                pll(len(te))
                print(te)
                pll(len(te))
    elif inp == "3":
        s_or_d = input("Do you want to remove a\n1. student\n2. test\n Enter 1/2: ")
        if s_or_d == "1":
            name = input("What is the name of the student: ")
            if name != "": # checks for not empty
                del data[name]
                updatefile(data)             
                te = name+" has been removed from the stduent test data table"            
                pll(len(te))
                print(te)
                pll(len(te))
        elif s_or_d == "2":
            name = input("What is the name of the student to remove the test from: ")
            test = input("What is the name of the test to remove from the student: ")
            if name != "" and test != "": # checks
                del data[name][test]
                updatefile(data)
                te = test+" has been remove from "+name+"'s test data table"
                pll(len(te))
                print(te)
                pll(len(te))
    elif inp == "4":
        break
    
