def find_outlier(n):
    i = 1
    
    if n[0] % 2 != n[1] % 2:
        if n[0] % 2 == n[2] % 2:
            return n[1]
        else:
            return n[0]

    while True:
        if n[i] % 2 == n[i+1] % 2:
            i += 1
        else:
            return n[i+1]

print(find_outlier([2,3,5,3,7,1]))

