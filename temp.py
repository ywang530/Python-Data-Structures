a = [1,None,2,3,None,None,5,None]

for i in range(len(a)):
    if a[i] == None and i != 0:
        a[i] = a[i-1]

print(a)

from heapq import heapify, heappop, heappush, nlargest
from collections import defaultdict

input = {'a':1,'b':2,'c':3,'d':4,'e':3,'f':4, 'g':5}

heap = []
inverseDict = defaultdict(list)
for k, v in input.items():
    if v not in inverseDict:
        heappush(heap, v)
        inverseDict[v].append(k)

print(heap)
print(inverseDict)

nthLargestVal = nlargest(2, heap)[-1]

print(nthLargestVal)
print(sorted(inverseDict[nthLargestVal])[0])