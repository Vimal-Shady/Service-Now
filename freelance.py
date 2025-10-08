from collections import defaultdict
def f(n,id,bid):
    x=defaultdict(lambda:float('inf'))
    for i,j in enumerate(id): x[j]=min(x[j],bid[i])
    return 0 if len(x)<n else sum(x.values())
print(f(2,[0,1,0,1,1],[4,74,47,744,7]))