t1 = [1,2,3,4,5]
t2 = ["a","b","c","d","e"]

print(dict(zip(t1,t2)))
    
#######################################################
print("\n")
      
sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
                }
            }
        }
    }

print(sampleDict["class"]["student"]["marks"]["history"])

#######################################################
print("\n")

sampleDict = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
    }

keysToRemove = ["name","salary"]

for item in keysToRemove:
    sampleDict.pop(item)

print(sampleDict)

#######################################################
print("\n")

sampleDict = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
    }

sampleDict["location"] = sampleDict.pop("city")

print(sampleDict)

#######################################################
print("\n")

def write(data):
    with open("data.txt","w") as file:
        file.write(data + "\n")
        
def read():
    with open("data.txt","r") as file:
        return file.read()
        
def append(data):
    with open("data.txt","a") as file:
        file.write(data + "\n")

def appendnl(data):
    with open("data.txt","a") as file:
        file.write("\n" + data)
        
write("hello")
appendnl("hehehe")
print(read())
