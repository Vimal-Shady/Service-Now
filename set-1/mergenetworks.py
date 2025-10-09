from collections import deque
def f(n,x,r):
    q=deque()
    q.append(r)
    l=-1
    vis=set()
    while q:
        k=len(q)
        for _ in range(k):
            nde=q.popleft()
            if nde in vis: continue
            vis.add(nde)
            for i in x[nde]: 
                if i in vis: continue
                q.append(i)
        l+=1
    return l
def merge(n1,af,at,n2,bf,bt):
    x=[[] for i in range(n1+1)]
    y=[[] for i in range(n2+1)]
    for i,j in enumerate(af): x[j].append(at[i]);x[at[i]].append(j)
    for i,j in enumerate(bf): y[j].append(bt[i]);y[bt[i]].append(j)
    net1=min(f(n1,x,i) for i in range(1,n1+1))
    net2=min(f(n2,y,i) for i in range(1,n2+1))
    return net1+net2+1

print(merge(3,[1,1],[2,3],3,[1,2],[2,3]))