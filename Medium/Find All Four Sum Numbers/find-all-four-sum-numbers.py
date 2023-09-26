#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, nums, k):
        # code here
        nums.sort()
        res=[]
        for i in range(len(nums)) :
            if i>0 and nums[i]==nums[i-1] :
                continue
            for j in range(i+1,len(nums)) :
                if j>i+1 and nums[j]==nums[j-1] :
                    continue
                l=j+1
                r=len(nums)-1
                while l<r :
                    t=nums[i]+nums[j]+nums[l]+nums[r]
                    if t==k :
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l +=1
                        while l<r and nums[l]==nums[l-1] :
                            l +=1
                    if t<k :
                        l +=1
                    else :
                        r -=1
        return res
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends