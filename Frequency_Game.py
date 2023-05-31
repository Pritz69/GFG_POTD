def LargButMinFreq(arr,n):
    #code here
    d=dict()
    for x in arr :
        d[x] = 1 + d.get(x,0)
    m = float('inf')
    for x in d :
        if d[x] < m :
            m = d[x]
    k= float('-inf')
    for x in d :
        if d[x] == m and x > k :
            k=x
    return k
