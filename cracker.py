import random

letters = "abcdefghijklmnopqrstuvwxyz"

def runcrack(password):
    length = len(password)
    letterlist = []
    word = ""
    for i in range(0,length):
        letterlist.append("a")

    print(letterlist)
    
    index = 0
    for i in letterlist:
        b = 0
        while b <= 25:
            letterlist[index] = letters[b]
            print(letterlist,index)
            b = b + 1
        index = index + 1
runcrack("abcd")
