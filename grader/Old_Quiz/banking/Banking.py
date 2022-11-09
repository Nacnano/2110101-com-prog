n = int(input())
accounts = {}
names = {}
for i in range(n):
    name, id, amount = input().split()
    accounts[id] = float(amount)
    names[id] = name


def output(id):
    print(names[id], "("+id+")", str(accounts[id]).rstrip('0').rstrip('.'))


while True:
    s = input()
    if s == "exit":
        break
    inputs = s.split()
    name, id, do = inputs[:3]
    if id not in accounts:
        accounts[id] = inputs[3]
        names[id] = name
        output(id)
        continue
    if names[id] != name:
        print("Transaction Failed")
        continue
    if do == "deposit":
        accounts[id] += float(inputs[3])
        output(id)
    elif do == "withdraw":
        amount = float(inputs[3])
        if amount > accounts[id]:
            print("Transaction Failed")
            continue
        accounts[id] += amount
        output(id)
    elif do == "transfer":
        amount = float(inputs[4])
        if amount > accounts[id]:
            print("Transaction Failed")
            continue
        accounts[id] -= amount
        accounts[inputs[3]] += amount
        output(id)
        output(inputs[3])
