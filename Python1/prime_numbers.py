import math
""" The module for detecting prymary numbers. Developed by Dmitry Pavlov """

def IsPrimaryNumber(N):
    """ The function detects input number is pripmary or not. """
    if N < 2:
        return False

    primarylist = [2, 3, 5]

    if N in primarylist:
        return True

    for i in primarylist:
        if (N % i == 0):
            return False

    start = primarylist[len(primarylist) - 1] + 2
    end = math.floor(math.sqrt(N)) + 1

    for i in range(start , end, 2):
        if (N % i == 0):
            return False

    return True

def PrimarySequience(N):
    """ The functions outputs primary numbers less than N. """
    for i in range(2, N + 1):
        if (IsPrimaryNumber(i)):
            print(i)

def PrimarySequience2(K, N):
    """ The functions outputs primary numbers more than K and less than N. """
    for i in range(K, N + 1):
        if (IsPrimaryNumber(i)):
            print(i)

def PiFunction(N):
    """ The function returns count of primary numbers less than N.  """
    c = 0
    for i in range(2, N + 1):
        if (IsPrimaryNumber(i)):
            c += 1

    return c

def PiFunction2(K, N):
    """ The function returns count of primary numbers between K and N.  """
    c = 0
    for i in range(K, N + 1):
        if (IsPrimaryNumber(i)):
            c += 1

    return c

def EuclidNod(K, N):
    """ The method returns the least common devider for integer numbers K and N """
    
    while K != 0 and N != 0 :
        if (N > K):
            N = N % K
        else:
            K = K % N

    return (K + N)

def LeastCommonMultiple(K, N):
    """ The method returns the least common multiple for two integer numbers """

    return K * N // EuclidNod(K, N)

def Euler(N):
    """ Eluler's function """

    counter = 1
    
    for i in range(2, N):
        if (EuclidNod(i, N) == 1):
            counter += 1

    return counter

def Factorial(N):
    """ The function returns factorial of the input number. N must be an integer number. """

    if N < 0:
        return 0
    
    if N < 2:
        return 1

    return N * Factorial(N-1)

def GetNextPrimary(N):
    """ The function return the nearest primary number more than N."""

    K = 0

    if N % 2 == 0:
        K = N + 1
    else:
        K = N + 2

    while not IsPrimaryNumber(K):
        K += 2

    return K        

def SplittingInteger(N):
    """ The function splits the input integer number to the composition of product of primary numbers """

    if N < 2 or IsPrimaryNumber(N):
        return N

    result = "{0}=".format(N)
    end = (N >> 1) + 1

    for i in range(2, end):       
        if IsPrimaryNumber(i):
            power = 0
            K = N           
            while K % i == 0:
                power += 1
                K = K // i
            if power == 1:
                result += "{0}*".format(i)
            elif power > 1:
                result += "{0}({1})*".format(i, power)
    
    return result[:  len(result) - 1]
