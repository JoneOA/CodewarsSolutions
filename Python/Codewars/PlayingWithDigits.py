def dig_pow(n, p):

    counter = 0
    sumOfPow = 0

    for y in str(n):
        sumOfPow += int(y)**(p+counter)
        counter += 1
    
    if sumOfPow % n == 0:
        return(int(sumOfPow/n))
    else:
        return -1
    

print(dig_pow(89,1))
