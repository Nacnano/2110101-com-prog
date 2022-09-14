s = input().strip()
valid = True
for c in s:
    if c not in ['A', 'T', 'C', 'G']:
        valid = False

q = input()

if not valid:
    print("Invalid DNA")
elif q == 'R':
    s = s.replace('A', 'T').replace('T', 'A').replace('C', 'G').replace('G', 'C')
    print(s)
elif q == 'F':
    print("A=", s.count('A'), ", T=", s.count('T'), ", ")
