def printFactors(x):
    print("You can only use one of these numbers: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

def takeSuitNumber(message, N):
    M = takeIntNumber(message,1)
    while((int(N/M)*M) != N):
        print("N is not dividable by M!")
        printFactors(N)
        return takeSuitNumber(message, N)
    return M

def takeIntNumber(message, low, high=1e6):
    user_input = input(message+" ")
    try:
        N = int(float(user_input))
    except ValueError:
        print("Not a valid number.")
        return takeIntNumber(message, low, high)
    while(N<low):
        print("Enter a number N>"+str(low))
        return takeIntNumber(message, low, high)
    while(N>high):
        print("Enter a number N<"+str(high))
        return takeIntNumber(message, low, high)
    return N
