from operator import neg
import heapq
def f(n,ff,x,y):
    arr=list(map(neg,ff))
    heapq.heapify(arr)
    cur=0
    i=0
    while arr and -arr[0]>=cur:
        i+=1
        f=heapq.heappop(arr)
        f+=x
        cur+=y
        if -f>0: heapq.heappush(arr,f)
    return i


f(5,[3,4,1,7,6],4,2)
f(5,[3,3,6,3,9],3,2)