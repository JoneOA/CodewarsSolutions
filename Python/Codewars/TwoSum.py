def two_sum(numbers, target):
    c = 0
    for a, b in enumerate(numbers):
        c = a + 1
        while c < len(numbers):
            if b + numbers[c] == target:
                return[a, c]
            c += 1

print(two_sum([1,2,3], 4))