class roman:
    def __init__(self, r):

    def __lt__(self, rhs):

    def __str__(self):
    def __int__(self):

    def __add__(self, rhs):


t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)
if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))
