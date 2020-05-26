def productFib(prod):

    fib = [0,1]
    count = 0

    while fib[0]*fib[1] <= prod:

        if prod == fib[0]*fib[1]:
            fib.sort()
            fib.append(True)
            return fib

        index = count % 2

        if index == 0:
            fib[index] += fib[index+1]
        else:
            fib[index] += fib[index-1]

        count += 1

    fib.sort().append(False)
    return fib

def productFibChris(prod):
    fib = [0,1]
    fibProd = fib[0] * fib[1]
    
    while fibProd < prod:
        min_pos = fib.index(min(fib))
        fib[min_pos] = fib[0] + fib[1] 
        fibProd = fib[0] * fib[1]
        
        if fibProd == prod:
            return [min(fib), max(fib), True]
        if fibProd > prod:
            return [min(fib), max(fib), False]
    if prod == 0: return [0,1,True]

print(productFib(9685))


