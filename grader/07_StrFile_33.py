def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0:
            break
        x = t.strip().split()
        if len(x) == 2:
            return x[0], x[1]
    return "", ""
