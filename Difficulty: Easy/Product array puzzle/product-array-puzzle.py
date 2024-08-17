#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        ans=[]
        p=1
        c=0
        for x in nums :
            if x==0 :
                c +=1
            else :
                p=p*x
        if c==0 :
            for x in nums :
                ans.append(p//x)
        elif c==1 :
            for x in nums :
                if x==0 :
                    ans.append(p)
                else :
                    ans.append(0)
        else :
            for x in nums :
                ans.append(0)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends