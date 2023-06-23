class Solution:
    def leastInterval(self, N, K, tasks):
        # Code here
        c={}
        for x in tasks :
            c[x] = c.get(x,0) + 1
        m=0
        for x in c :
            m=max(m,c[x])
        cnt=0
        for x in c :
            if c[x]==m :
                cnt +=1
        ans = max(N, ((m-1)*(1+K) + cnt))
        return ans
