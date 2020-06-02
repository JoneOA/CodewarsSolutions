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
            if preOutput[counter][0] % num[0] == 0 and preOutput[counter][0]>num[0]:
                preOutput.pop(counter)
                counter -= 1
            counter+=1
 
    i=0
    currentNum = preOutput[0]
    total = 0

    while i < len(preOutput):
        if currentNum[0] == preOutput[i][0]:
            total += preOutput[i][1]
        else:
            output.append([currentNum[0],total])
            currentNum = preOutput[i]
            total = currentNum[1]
        i+=1
    output.append([currentNum[0], total])    
    
    return output
    
print(sum_for_list([15, 21, 24, 30, -45]))
