def array_diff(a, b):
    c = []
    for x in a:
        exists = 0
        for y in b:
            if x == y:
                exists = 1
        if exists == 0:
            c.append(x)
    return c