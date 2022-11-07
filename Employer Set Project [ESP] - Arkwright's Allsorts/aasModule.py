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

appendfile("") # creates a file if there isnt one already, if there is one it does nothing

data = {}

try:
    data = eval(readfile())
except:
    data = {}


