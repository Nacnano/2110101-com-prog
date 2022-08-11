def sqrt_n_times(x, n):
    return x**(1/2**n)


def cube_root(y):
    return sqrt_n_times(y, 2)*sqrt_n_times(y, 4)*sqrt_n_times(y, 6)*sqrt_n_times(y, 8)*sqrt_n_times(y, 10)*sqrt_n_times(y, 12)*sqrt_n_times(y, 14)*sqrt_n_times(y, 16)
    # return sqrt_n_times(sqrt_n_times(sqrt_n_times(sqrt_n_times(sqrt_n_times(sqrt_n_times(sqrt_n_times(y, 2), 2), 2), 2), 2), 2), 2)


def main():
    q = float(input())
    print(cube_root(q))


exec(input())
