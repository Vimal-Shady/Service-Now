from collections import defaultdict,Counter,deque
# def f(s):
#     r=Counter(s)
#     f=len(s)%2
#     x=[]
#     for i,j in list(r.items()):
#         if j%2==0: continue
#         x.append(i); r[i]-=1
#         if r[i]==0: r.pop(i)
#     x.sort()
#     while len(x)>f:
#         a,b=x.pop(0),x.pop()
#         r[min(a,b)]+=2
#     k=[[i,j] for i,j in r.items()]
#     k.sort()
#     y="".join(i*(j//2) for i,j in k)
#     return y+(x[0] if x else "")+y[::-1]

def f(s):
    r=Counter(s)
    x=deque(sorted(i for i,j in r.items() if j%2))
    f=len(s)%2
    while len(x)>f:
        a,b=x.popleft(),x.pop()
        j=min(a,b)
        r[j]+=2;r[a]-=1;r[b]-=1
        if r[a]==0: r.pop(a)
        if r[b]==0: r.pop(b)
    g="".join(i*(j//2) for i,j in sorted(r.items()))
    return g+(x[0] if x else "")+g[::-1]


t=["azzzbbb","fhaigh"]
for i in t: print(f(i))