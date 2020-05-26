def create_phone_number(a):
    num = "("
    x = 0
    while x < 3:
        num += str(a[x])
        x += 1
        print(x)
    num += ") "

    while x < 6:
        num += str(a[x])
        x += 1
        print(x)
    
    num += "-"

    while x < 10:
        num += str(a[x])
        x += 1
    return num

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))