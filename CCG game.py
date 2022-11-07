import random
import time

colours = ["red","green","blue","yellow"]

plrPoints = 0
comPoints = 0
    
while True:
    print("")
    
    num = 1
    for colour in colours:
        print(num,colour)
        num = num+1
    
    plrInp = input("\nEnter a number to pick a colour from above: ")
    
    while True:
        if not plrInp.isnumeric():
            plrInp = input("\nThat is not a colour number! Enter a number from 1 to 4: ")
        else:
            plrInp = int(plrInp)
            if (plrInp < 1) or (plrInp>4):
                plrInp = input("\nThat is not a colour number! Enter a number from 1 to 4: ")
            else:
                break

    plrInp = int(plrInp)
        
    plrChoice = colours[plrInp-1]
    
    time.sleep(0.5)
    
    comChoice = colours[random.randint(0,3)]
    print("\nThe computers choice was " + comChoice)
    
    if plrChoice == comChoice:
        plrPoints += 1
        print("\nYou have guessed the correct colour")
        time.sleep(1)
        print("\nPlayer points =", plrPoints)
        print("Computer points =", comPoints,)
        time.sleep(1)
    else:
        comPoints += 1
        print("\nYou have guessed the wrong colour")
        time.sleep(1)
        print("\nPlayer points =", plrPoints)
        print("Computer points =", comPoints)
        time.sleep(1)
        
    if plrPoints == 5:
        kpInp = input("\nYou have won! Do you want to keep playing yes/no: ")
        while (kpInp != "yes") and (kpInp != "no"):
            kpInp = input("\nThat is not a valid choice, please only choose yes/no: ")
        if kpInp == "no":
            break
        
        plrPoints = 0
        comPoints = 0
        print("\nPlayer points =", plrPoints)
        print("Computer points =", comPoints)
    elif comPoints == 5:
        kpInp = input("\nThe computer has won! Do you want to keep playing yes/no: ")
        while (kpInp != "yes") and (kpInp != "no"):
            kpInp = input("\nThat is not a valid choice, please only choose yes/no: ")
        if kpInp == "no":
            break
        
        plrPoints = 0
        comPoints = 0
        print("\nPlayer points =", plrPoints)
        print("Computer points =", comPoints)
        time.sleep(1)

print("\nThanks for playing")
