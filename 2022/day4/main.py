def buildRange(val):
    locs = val.split("-")
    start, end = int(locs[0]), int(locs[1])
    return [x for x in range(start, end+1)]

overlap = 0
with open("input.txt", "r") as f:
    for item in f.readlines():
        elves = item.split(",")
        e1, e2 = elves[0], elves[1]
        e1_range, e2_range = buildRange(e1), buildRange(e2)
        e1_s = e2_s = 0
        found_eq = False
        broke_found = False
        size = 0
        while e1_s < len(e1_range) and e2_s < len(e2_range):
            e1_val, e2_val = e1_range[e1_s], e2_range[e2_s]

            if e1_val != e2_val and not found_eq:
                if e1_val < e2_val:
                    e1_s += 1
                else:
                    e2_s += 1
            elif e1_val != e2_val and found_eq:
                broke_found = True
                break
            else:
                size += 1
                e1_s += 1
                e2_s += 1
                found_eq = True
        if size == len(e2_range) or size == len(e1_range):
            print(e1_range, e2_range)
            overlap += 1


print(overlap)

overlap = 0
with open("input.txt", "r") as f:
    for item in f.readlines():
        elves = item.split(",")
        e1, e2 = elves[0], elves[1]
        e1_range, e2_range = buildRange(e1), buildRange(e2)
        e1_s = e2_s = 0
        found_eq = False
        broke_found = False
        size = 0
        while e1_s < len(e1_range) and e2_s < len(e2_range):
            e1_val, e2_val = e1_range[e1_s], e2_range[e2_s]

            if e1_val != e2_val and not found_eq:
                if e1_val < e2_val:
                    e1_s += 1
                else:
                    e2_s += 1
            elif e1_val != e2_val and found_eq:
                broke_found = True
                break
            else:
                size += 1
                e1_s += 1
                e2_s += 1
                found_eq = True
        if size:
            overlap += 1


print(overlap)
