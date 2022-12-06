def priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

sum = 0

with open("input.txt", "r") as f:
    for item in f.readlines():
        item = item.strip()
        mid = len(item) // 2

        firstSack = set(item[0:mid])
        secondSack = set(item[mid:len(item)])
        for item in firstSack:
            if item in secondSack:
                sum += priority(item)
                break


sum = 0
elves = []
i = 0
with open("input.txt", "r") as f:
    for item in f.readlines():
        elves.append(set(item.strip()))

while i < len(elves):
    for item in elves[i]:
        if item in elves[i+1] and item in elves[i+2]:
            sum += priority(item)
            break

    i += 3

print(sum)
