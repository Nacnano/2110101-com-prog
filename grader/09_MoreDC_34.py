def pattern1(nrows, ncols):
    ret = []
    for i in range(nrows):
        ret += [list(range(i*ncols+1, (i+1)*ncols+1))]
    return ret


def pattern2(nrows, ncols):
    ret = []
    for i in range(nrows):
        ret += [list(range(i+1, nrows*ncols+1, nrows))]
    return ret


def pattern3(N):
    ret = []
    for i in range(N):
        ret += [[0]*i + list(range(i*N-int((i-1)*(i)/2)+1, (i+1)*N-int(i*(i+1)/2)+1))]
    return ret


def pattern4(N):
    ret = []
    for i in range(N):
        ret += [[0]*i]
        num = int((i+1)*(i+2)/2-i)
        for j in range(N-i):
            ret[i] += [num]
            num += j+i+2
    return ret


def pattern5(N):
    ret = []
    for i in range(N):
        ret += [[0]*i]
        num = i+1
        for j in range(N-i):
            ret[i] += [num]
            num += N-j
    return ret


def pattern6(N):
    ret = []
    return ret


exec(input().strip())
