def checkIfPrime(number):
    for x in range(2,number):
        if (number%2==0):
            return False
    return True
