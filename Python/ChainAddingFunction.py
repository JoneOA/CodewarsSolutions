sumArray = []

def add(x):
    total = 0
    sumArray.append(x)
    for a in sumArray:
        total += a
    
    return total

add(2)