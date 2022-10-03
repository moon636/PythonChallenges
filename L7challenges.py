t1 = [1,2,3,4,5]
t2 = ["a","b","c","d","e"]

print(dict(zip(t1,t2)))

#######################################################

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

sampleDict = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
    }

sampleDict["location"] = sampleDict.pop("city")

print(sampleDict)
