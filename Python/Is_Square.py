import math
def is_square(n):
    if n < 0:
        return False
    elif (math.sqrt(n) % 1) == 0:
        return True
    else:
        return False
    


print(is_square(4))
print(is_square(26))