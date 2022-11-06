n = int(input())
parties = []
for i in range(n):
    parties += [input()]

partyOf = {}
memberInParty = {}
n = int(input())
for i in range(n):
    name, party = input().split()
    partyOf[name] = party
    if party in memberInParty:
        memberInParty[party] += [name]
    else:
        memberInParty[party] = [name]

n = int(input())
results = {}
individual = {}
for i in range(n):
    name, result = input().split()
    individual[name] = result
    party = partyOf[name]
    if party in results:
        if result in results[party]:
            results[party][result] += 1
        else:
            results[party][result] = 1
    else:
        results[party] = {result: 1}
types = ['Y', 'N', 'X']
for party in parties:
    print(party)
    result = []
    for type in types:
        if type not in results[party]:
            count = 0
        else:
            count = results[party][type]
        result += [(count, type)]
    result.sort()
    if result[-1][0] == result[-2][0]:
        print("Inconclusive")
        continue
    cobra = []
    for member in memberInParty[party]:
        if member not in individual:
            continue
        if individual[member] != result[-1][1]:
            cobra += [member]
    cobra.sort()
    if len(cobra):
        print(", ".join(cobra))
    else:
        print("No Cobra")
