import math
def list_squared(m, n):

    finalOutput = []

    for x in range(m,n+1):

        total = 0
        factors = []

        upperLim = int(math.sqrt(x+1))

        for i in range (1, upperLim+1):
            if x % i == 0:
                factors.append(i)
                if int(x/i) != i:
                    factors.append(int(x/i))
                
        for i in factors:
            total += i*i

        if int(math.sqrt(total))*int(math.sqrt(total)) == total:
            finalOutput.append([x,total])

    return finalOutput


print(list_squared(1, 52))
