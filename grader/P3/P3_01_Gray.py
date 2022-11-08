n = int(input())
k = int(input())
nvalid = n < 0 or type(n) == float
kvalid = k < 1
if nvalid and kvalid:
    print("Invalid n and k ")
elif nvalid:
    print("Invalid n")
elif kvalid:
    print("Invalid k")

print("".join((str(i+1) + "-"*n) for i in range(k)))
