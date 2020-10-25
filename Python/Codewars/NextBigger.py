def next_bigger(n):

    nToArray = []
    prevNumbers = []
    nextNumCheck = "9"
    finalNumber = ""
    y = str(n)

    for x in y:
        nToArray.append(x)

    length = len(y)
    count = 0
    out = 0

    for x in y:

        prevNumbers.append(y[length - (count+1)])

        for a in prevNumbers:

            if a > y[length - (count+1)] and a <= nextNumCheck:

                nextNumCheck = a

                nToArray[length - (count+1)] = a

                prevNumbers.remove(a)

                out = 1
                break

        if out == 1:
            break

        count += 1

    while count > 0:

        smallest = "9"

        i = 0
        
        while i < len(prevNumbers):
            
            if prevNumbers[i] <= smallest:
                
                smallest = prevNumbers[i]

                nToArray[-(count)] = prevNumbers[i]

            i += 1

        prevNumbers.remove(smallest)

        count -= 1

    i=0
    for x in nToArray:
        finalNumber += nToArray[i]
        i+=1

    if int(finalNumber) > n:
         return(int(finalNumber))
    
    return(-1)

print(next_bigger(4125856302575215875210))