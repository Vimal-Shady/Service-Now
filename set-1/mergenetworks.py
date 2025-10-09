from collections import defaultdict,deque,Counter

def f(n,x,nde):
    

def merge(n1,af,at,n2,bf,bt):
    x=[[] for i in range(n1+1)]
    y=[[] for i in range(n2+1)]
    for i,j in enumerate(af): x[j].append(at[i]);x[at[i]].append(j)
    for i,j in enumerate(bf): y[j].append(bt[i]);y[bt[i]].append(j)
    l=[f(n1,x,i) for i in range(1,n1+1)]
    print(l)
    r=[f(n2,y,i) for i in range(1,n2+1)]
    print(r)







merge(3,[1,1],[2,3],3,[1,2],[2,3])