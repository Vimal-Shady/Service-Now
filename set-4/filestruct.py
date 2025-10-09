from collections import defaultdict,deque

def f(edges,q):
    x=defaultdict(set); x['folder-1']
    pre=defaultdict(int)
    for i,j in edges: x[i].add(j)
    def mk(i,j):
        x[i].add(j)
        pre[j]=i;x[i]
    def rm(i):
        q=deque([i])
        dt=[]
        while q:
            nde=q.popleft()
            dt.append(nde)
            for j in x[nde]: q.append(j)
        if i in pre: x[pre[i]].discard(i);pre.pop(i)
        for h in dt:
            if h in x:del x[h]
            if h in x[pre[h]]: x[pre[h]].discard(h)

    def cnt(nde):
        q=deque([nde])
        r=-1
        while q:
            nde=q.popleft()
            r+=1
            for i in x[nde]: q.append(i)
        return r
    for i in q:
        s=i.split()
        if len(s)==2:
            if s[0]=="rmdir": rm(s[1])
            elif s[0]=="countd": print(cnt(s[1]))
        elif len(s)==3 and s[0]=="mkdir": mk(s[1],s[2])
    print(pre)
    




edges=[["folder-1","a"],["folder-1","b"],["folder-1","c"],["a","d"],["a","e"],["e","f"],["c","g"]]
q=["mkdir d h","rmdir e","countd a"]
f(edges,q)