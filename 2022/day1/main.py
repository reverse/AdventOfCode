from heapq import *

data = []
with open("input1.txt", "r") as f:
    data = f.readlines()

heap = []

i = 0
elves = 1
temp = []
while i < len(data):
    if data[i] == '\n':
        heappush(heap, [-sum(temp), elves])
        elves += 1
        temp = []
    else:
        temp.append(int(data[i]))
    i+=1

sum = 0
for i in range(3):
    data = heappop(heap)
    data[0] = -data[0]
    sum += data[0]
print(sum)

