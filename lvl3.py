statuses = {
"Alice": "online",
"Bob": "offline",
"Eve": "online",
}

def online_count(dic):
    count = 0
    for i in statuses:
        if statuses[i] == "online":
            count += 1
    return count

print(online_count(statuses))

def only_ints(a,b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False

print(only_ints(1,2))
print(only_ints("a",2))
