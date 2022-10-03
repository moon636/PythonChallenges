
while True:
    name = input("What is your name? ")
    if name == "0" or  name.lower() == "exit":
        break
    print(name+" is a great name!")

for i in range(1,51):
    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)
    
def highestnum(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c>b:
        print(c)
    else:
        print("all equal")

