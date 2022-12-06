with open("input.txt", "r") as f:
    for item in f.readlines():
        chars = 0
        window_start = 0
        for window_end in range(1, len(item)):
            chars+=1
            size = window_end - window_start
            if size < 4:
                continue
            print(chars, item[window_start:window_end])
            if len(set(item[window_start:window_end])) < 4:
                   window_start += 1
            else:
                print(chars)
                break

with open("input.txt", "r") as f:
    for item in f.readlines():
        chars = 0
        window_start = 0
        for window_end in range(1, len(item)):
            chars+=1
            size = window_end - window_start
            if size < 14:
                continue
            print(chars, item[window_start:window_end])
            if len(set(item[window_start:window_end])) < 14:
                   window_start += 1
            else:
                print(chars)
                break
