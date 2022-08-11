n =
m =
map = [["." for i in range(m+10)] for j in range(n+10)]


def dfs(x, y, d):
    if x <= 0 or y <= 0 or y >= n or x >= m:
        return
    if map[y-1][x] == '/' or map[y-1][x] == '\\' or map[y-1][x] == '#':
        map[y][x] = '#'
    else:
        if d == -1:
            map[y][x-1] = '/'
            map[y][x] == '#'
        else:
            map[y][x+1] = '\\'
            map[y][x] = '#'

    dfs(x+d, y+1, d)
    dfs(x, y+1, d)


def start(x, y):
    dfs(x, y, -1)
    dfs(x+1, y, 1)


start(1, 1)
start()

map[0][0] = map[0][m-1] = map[n-1][0] = map[n-1][m-1] = "+"

for i in range(1, m-1):
    map[0][i] = '-'
    map[n-1][i] = '-'

for i in range(1, n-1):
    map[i][0] = '|'
    map[i][m-1] = '|'


for i in range(n):
    for j in range(m):
        print(map[i][j], end="")
    print("")
