class roman:
    def __init__(self, r):
        if type(r) == str:
            self.roman = r
            # self.dec = int(self)
        else:
            self.dec = r
            self.roman = str(self)

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        return self

    def __int__(self):
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        ret = 0
        mode = 1
        while i < len(self.roman)-1:
            if values[self.roman[i]] < values[self.roman[i+1]]:
                ret += values[self.roman[i]]
                j = i + 1
                mode = -1
                while j < len(self.roman)-1:
                    if values[self.roman[j]] > values[self.roman[j+1]]:
                        i = j
                        mode = 1
            else:
                ret += values[self.roman[i]]
                mode = 1
        ret += mode*values[self.roman[-1]]
        return ret

    def __add__(self, rhs):
        return roman(int(self)+int(rhs))


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
