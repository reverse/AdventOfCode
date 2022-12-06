import re

stacks = []
i = 0
startMoving = False
with open("input.txt", "r") as f:
    for item in f.readlines():
        if item == '\n':
            startMoving = True
            print(stacks)
            continue

        if not startMoving:
            results = re.findall(r"\[(.*?)\]",item)
            for i, item in enumerate(results):
                if len(stacks) <= i:
                    stacks.append([])

                if item != '0': stacks[i].append(item)

            i+=1
        else:
            operations = item.split(" ")
            amount = int(operations[1])
            from_v = int(operations[3])
            to_v = int(operations[len(operations)-1])
            print(amount, from_v, to_v)

            moved = amount
            while moved > 0 and stacks[from_v-1]:
                item = stacks[from_v-1].pop(0)
                stacks[to_v-1].insert(0, item)

                moved -= 1

res = ""
for item in stacks:
    res += item[0]
print(res)

stacks = []
i = 0
startMoving = False
with open("input.txt", "r") as f:
    for item in f.readlines():
        if item == '\n':
            startMoving = True
            print(stacks)
            continue

        if not startMoving:
            results = re.findall(r"\[(.*?)\]",item)
            for i, item in enumerate(results):
                if len(stacks) <= i:
                    stacks.append([])

                if item != '0': stacks[i].append(item)

            i+=1
        else:
            operations = item.split(" ")
            amount = int(operations[1])
            from_v = int(operations[3])
            to_v = int(operations[len(operations)-1])
            print(amount, from_v, to_v)

            moved = amount
            while moved > 0 and stacks[from_v-1]:
                item = stacks[from_v-1].pop(0+moved-1)
                stacks[to_v-1].insert(0, item)

                moved -= 1
res = ""
for item in stacks:
    res += item[0]
print(res)
