def ask(string,yes):
    a = input(string)
    if a.lower() == "yes":
        print(yes)
    else:
        return True

if ask("Does it have 2 horns and 1 on the nose ","Triceratops"):
    if ask("Does it have short arms and a long tail ","tryannasaurus"):
        if ask("Does it have a long neck with tiny horns ","nigersaurus"):
            if ask("Does it have big horns on its back ","stegosaurus"):
                print("mosasaurus")
                
    
