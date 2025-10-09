def f(s,k): 
    fj=[chr(i) for i in range(65,91)]
    ans="".join(fj[abs(ord(i)-65)-k] for i in s)
    print(ans)
f("VTAOG",2)