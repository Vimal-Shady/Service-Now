
cells=[20,30,40]
import heapq
def f(arr):
    heapq.heapify(arr)
    prev=heapq.heappop(arr)
    ans=0
    while len(arr)>=1:
        x=heapq.heappop(arr)
        ans+=x+prev
        prev+=x
    return ans
print(f(cells))

#reduce array
print('reduce array')
print(f([10,20,30]))