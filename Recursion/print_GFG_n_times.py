def gfg(n):
    if n==0:
        return
    print("GFG",end=' ')
    gfg(n-1)
gfg(5)