# assign data
mydata = [
    ["Nikhil", ""],
    ["Ravi", ""],
    ["Manish", ""],
      ["Prince", ""]
]
 
# create header
head = ["Name", "City"]
 
# display table
def line(length):
    string = "-"*length
    print(string)

def nl():
    print("\n")

line(30)
print("|                                                 | List | Array | Tuple |")
line(30)
print("| Is it mutable?                                  |      |       |       |")
print("| Can we change the size after creation?          |      |       |       |")
print("| Can items in the list be changed?               |      |       |       |")
print("| How many different types of data can be stored? |      |       |       |")
