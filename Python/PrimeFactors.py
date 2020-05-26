import math

def primeFactors(n):
    
    primeFactorsList = []
    exponentList = []
    
    finalString = ""

    answer = n

    nextPrime = 2

    while answer != 1:
        counter = 0

        upperLim = int(math.sqrt(nextPrime+1))

        if nextPrime == 2:
            for i in range(2, nextPrime):
                if nextPrime % i == 0:
                    counter += 1
        else:
            for i in range(2, upperLim):
                if nextPrime % i == 0:
                    counter += 2
        
        if counter == 0:
            while answer % nextPrime == 0:
            
                answer = answer/nextPrime
                primeFactorsList.append(nextPrime)
            
            if nextPrime > math.sqrt(answer+1)+1:
                primeFactorsList.append(int(answer))
                answer = answer/answer
                
        if nextPrime == 2:
            nextPrime += 1
        else:
            nextPrime +=2



        print(primeFactorsList)

    firstCheck = 0
    exponent = 0
    index = 0
    length = len(primeFactorsList)

    while exponent < length:
        if primeFactorsList[index] != firstCheck:
            firstCheck = primeFactorsList[index]
            exponentList.append(primeFactorsList.count(primeFactorsList[index]))
            index += 1
        else:
            primeFactorsList.pop(index)

        exponent += 1

    index = 0

    for i in primeFactorsList:
        if exponentList[index] == 1:
            finalString += "("+str(primeFactorsList[index])+")"
        else:
            finalString += "("+str(primeFactorsList[index])+"**"+str(exponentList[index])+")"    
        index += 1

    return finalString


def primeFactors2(n):
    ret = ''
    for i in range(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret

print(primeFactors(50675))