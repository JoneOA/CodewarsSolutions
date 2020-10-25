import itertools

def get_pins(observed):


    pinpad = [[1,2,3],[4,5,6],[7,8,9],["=",0,"="]]
    bum = []
    digits = []
    output = []

    shwoop = {}

    for num in observed:
        x = 0
        while x < 4:
            y = 0
            while y < 3:
                if int(num) == pinpad[x][y]:
                    bum.append([x,y])
                y += 1
            x += 1

    i = 0

    while i < len(bum):
        count = 1
        noop = ''
        if bum[i][0] != 0:
            digits.append(pinpad[bum[i][0]-1][bum[i][1]])
            count += 1
        if bum[i][1] != 0 and pinpad[bum[i][0]][bum[i][1]] != 0:
            digits.append(pinpad[bum[i][0]][bum[i][1]-1])
            count += 1
        digits.append(pinpad[bum[i][0]][bum[i][1]])
        if bum[i][1] != 2 and pinpad[bum[i][0]][bum[i][1]] != 0:
            digits.append(pinpad[bum[i][0]][bum[i][1]+1])
            count += 1
        if bum[i][0] != 3 and (pinpad[bum[i][0]][bum[i][1]] != 7 and pinpad[bum[i][0]][bum[i][1]] != 9):
            digits.append(pinpad[bum[i][0]+1][bum[i][1]])
            count += 1
        i += 1
        noop = str(i)
        shwoop[noop] = digits
        digits = []

    output = list(itertools.product(*shwoop.values()))

    final = []

    for poss in output:
        temp = ''
        for num in poss:
            temp += str(num)
        final.append(temp)
    
    print(final)
    
    return final

get_pins('257')