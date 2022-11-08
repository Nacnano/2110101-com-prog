n = int(input())
k = int(input())
nvalid = n < 0 or type(n) == float
kvalid = k < 1
if nvalid and kvalid:
    print("Invalid n and k ")
    exit(0)
elif nvalid:
    print("Invalid n")
    exit(0)
elif kvalid:
    print("Invalid k")
    exit(0)

print("".join((str(i+1) + "-"*(n-len(str(i+1))+1)) for i in range(k-1))+str(k)+"-"*(n-1-len(str(k))+1))

codes = [""]
for i in range(n):
    codes = codes+codes[::-1]
    for j in range(len(codes)):
        if j < len(codes)//2:
            codes[j] = "0" + codes[j]
        else:
            codes[j] = "1" + codes[j]
for i in range(len(codes)):
    print(codes[i], end="")
    if (i+1) % k == 0 or i == len(codes)-1:
        print()
    else:
        print(end=",")
