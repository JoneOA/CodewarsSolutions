def solution(n):
    binaryN = ''
    largest0 = 0
    consecutive0 = 0
    
    while n != 0:
        if n%2 == 1:
            binaryN = '1' + binaryN
            n = n/2 - 0.5
        else:
            binaryN = '0' + binaryN
            n = n/2
        
    for digit in binaryN:
        if digit == '0':
            consecutive0 += 1
        else:
            if consecutive0 > largest0:
                largest0 = consecutive0
            consecutive0 = 0
    
    print(binaryN)
    return(largest0)

print(solution(113))

def newAttempt(n):
    count = 0
    biggu = 0

    while n != 1:
        if n%2 == 1:
            n = n/2 - 0.5
            if count > biggu:
                biggu = count
            count = 0
        else:
            n = n/2
            count += 1
    
    return biggu

print(newAttempt(113))