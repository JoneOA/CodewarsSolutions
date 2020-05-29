def sum_for_list(lst):

    preOutput =[]
    output = []

    for num in lst:
        for i in range (2, abs(num) + 1):
                if num % i == 0:
                    preOutput.append([i, num])

    preOutput.sort()

    for num in preOutput:
        counter = preOutput.index(num)+1
        while counter < len(preOutput):
            checkPrime = preOutput[counter]
            if checkPrime[0] % num[0] == 0 and checkPrime[0]>num[0]:
                preOutput.pop(counter)
                counter -= 1
            counter+=1
 
    i=0
    currentNum = preOutput[0]
    checkNum = []
    total = 0

    while i < len(preOutput):
        checkNum = preOutput[i]
        if currentNum[0] == checkNum[0]:
            total += checkNum[1]
        else:
            output.append([currentNum[0],total])
            currentNum = preOutput[i]
            total = currentNum[1]
        i+=1
    output.append([currentNum[0], total])    
    
    return output
    
print(sum_for_list([15, 21, 24, 30, -45]))
