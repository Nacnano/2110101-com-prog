s = input()
list_char = []
list_count = []
last = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] == last:
        count += 1
    else:
        list_char.append(last)
        list_count.append(count)
        last = s[i]
        count = 1
if s[-1] != s[-2]:
    list_char.append(s[-1])
    list_count.append(1)
for i in range(len(list_char)):
    print(list_char[i] + " " + str(list_count[i]) + " ", end="")
