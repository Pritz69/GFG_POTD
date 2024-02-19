#User function Template for python3
import heapq
class Solution:
    def minValue(self, s, k):
        # code here
        d={}
        for x in s:
            d[x]=d.get(x,0)+1
        d=dict(sorted(d.items(),key=lambda x:x[1]))
        h=[]
        for x in d :
            h.append(-d[x])
        heapq.heapify(h)
        c=0
        while  c!=k :
            v=heapq.heappop(h)
            #print(v)
            heapq.heappush(h,v+1)
            c +=1
        s=0
        for x in h :
            s += x*x
        return s
     
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends