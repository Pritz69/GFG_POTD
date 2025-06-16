class Solution:
    def minCost(self, heights, cost):
        # code here
        def calc(m):
            res=0
            for i,h in enumerate(heights):
                res+=abs(h-m)*cost[i]
            return res
            
        low=min(heights)
        high=max(heights)
        res=float('inf')
        while(low<=high):
            mid=(low+high)//2
            c1=calc(mid-1)
            c2=calc(mid)
            c3=calc(mid+1)
            if c1>=c2<=c3:
                res=c2
                break
            elif(c1>=c2>=c3):
                low=mid+1
            else:
                high=mid-1
        return res
        
        
        #The total cost function is convex (shaped like a valley). This means:
        #As you try different values of h, the total cost will first decrease, reach a minimum, and then increase again.
        #So, there’s only one optimal height which gives the minimum total cost.
