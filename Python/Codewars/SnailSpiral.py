def snail(snail_map):
    
    position = [0,0]
    innerCircle = 0
    test = [[]]

    while len(snail_map)*len(snail_map[0]) - len(test) > 1:

        while position[0] + 1 < len(snail_map[0]) - innerCircle:
            test.append(snail_map[position[1]][position[0]])
            position[0] += 1

        while position[1] + 1 < len(snail_map) - innerCircle:
            test.append(snail_map[position[1]][position[0]])
            position[1] += 1

        while position[0] > innerCircle:
            test.append(snail_map[position[1]][position[0]])
            position[0] -= 1

        while position[1] > innerCircle + 1:
            test.append(snail_map[position[1]][position[0]])
            position[1] -= 1
        
        innerCircle += 1

    if snail_map[0]:
        test.append(snail_map[position[1]][position[0]])
    
    return test

array = [[1,2,3],[8,9,4],[7,6,5]]
print(snail(array))