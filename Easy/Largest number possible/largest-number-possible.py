#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        n=[9]*N
        s=(9*N)
        d=s-S
        if d <0 or (S==0 and N!=1):
            return -1
        f=0
        #print(n,s,d)
        for i in range(len(n)-1,-1,-1) :
            if d >= 9 :
                n[i] -=9
                d -=9
            else :
                n[i] -=d
                d = 0
        ans=""
        for x in n :
            ans += str(x)
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends