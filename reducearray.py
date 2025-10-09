cells=[10,20,30]
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