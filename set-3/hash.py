def f(url,s,k):
    sf=[url[i:i+k] for i in range(0,len(url),k)]
    d={chr(i):abs(97-i) for i in range(97,123)}
    d[":"]=26;d["/"]=27;d["."]=28
    res=""
    for i in sf:
        r=sum(d[j] for j in i)
        res+=s[r%len(s)]
    return res

print(f("https://xyz.com","pqrst",4))