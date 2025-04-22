import heapq

L = [30,20,10,11,88,99]

heapq.heapify(L)
print(L)
p = heapq.heappop(L)
print(p)
heapq.heappush(L, 88)
heapq.heappush(L, 88)
print(L)

heapq.heappush(L, 88)
heapq.heappop(L)
print(L)
L1 = heapq.nlargest(2,L)
print(L1)
L2 = heapq.nsmallest(2,L)
print(L2)
print(heapq.heapreplace(L, 101))
print(L)
