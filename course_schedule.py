# 207. Course Schedule
#Input: 2, [[1,0],[0,1]]
from collections import deque

num =2
prerequisites = [[0,1]]

# make the hash map
neigbors = {i:set() for i in range(num)}
indegrees = {i:0 for i in range(num)}

for first, second in prerequisites:
    neigbors[second].add(first)

for node in indegrees:
    for neigbor in neigbors[node]:
        indegrees[node]+=1

queue = deque()

for node in indegrees:
    if indegrees[node]==0:
        queue.append(node)

count = 0
while queue:
    node = queue.popleft()
    count += 1
    for neigbor in neigbors[node]:
        indegrees[neigbor] -= 1
        if indegrees[neigbor]==0:
            queue.append(neigbor)

count == num

null_list = ['', '']
if null_list:
    print(True)
else:
    print(False)
