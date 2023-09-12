#User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        # code here 
        s=0
        i=1
        while (i*i) <= N :
            if N%i==0 :
                s +=i
            if i != N//i and N%(N//i)==0:
                s += (N//i)
            i +=1
        return 1 if (s-N)==N else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends