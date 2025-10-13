from collections import defaultdict
def f(dct,s):
    a,b=s.split(".")
    print(dct[a][b])

#test

x=defaultdict(lambda:defaultdict(int))
x["car"]["wheels"]=2
x["car"]["gears"]=5
f(x,"car.gears")