from collections import deque
# O(N^2)
# def f(n,x,r):
#     q=deque()
#     q.append(r)
#     l=-1
#     vis=set()
#     while q:
#         k=len(q)
#         for _ in range(k):
#             nde=q.popleft()
#             if nde in vis: continue
#             vis.add(nde)
#             for i in x[nde]: 
#                 if i in vis: continue
#                 q.append(i)
#         l+=1
#     return l
# O(N+E)
def f(n,x,r):
    q=deque([(r,0)])
    vis=set()
    fr,mxd=r,0
    while q:
        nde,d=q.popleft()
        if d>mxd: fr=nde;mxd=d
        for i in x[nde]:
            if i in vis: continue
            vis.add(i)
            q.append((i,d+1))
    return fr,mxd
def k(n,x):
    a,ad=f(n,x,2)
    b,bd=f(n,x,a)
    return (bd+1)//2

def merge(n1,af,at,n2,bf,bt):
    x=[[] for i in range(n1+1)]
    y=[[] for i in range(n2+1)]
    for i,j in enumerate(af): x[j].append(at[i]);x[at[i]].append(j)
    for i,j in enumerate(bf): y[j].append(bt[i]);y[bt[i]].append(j)
    net1=k(n1,x)
    net2=k(n2,y)
    return net1+net2+1

print(merge(3,[1,1],[2,3],3,[1,2],[2,3]))