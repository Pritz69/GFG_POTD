#User function Template for python3

class Solution:
    def numberOfPath (self, n, k, arr):
        # code here
        n=len(arr)
        def rec(i,j,s) :
            if i ==n or j==n :
                return 0
            s +=arr[i][j]
            if s==k and (i==n-1 and j==n-1) :
                return 1
            if s > k :
                return 0
            if (i,j,s) in dp :
                return dp[(i,j,s)]
            a=rec(i+1,j,s)
            b=rec(i,j+1,s)
            dp[(i,j,s)]=a+b
            return a+b
            
        dp={}
        return rec(0,0,0)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)


# } Driver Code Ends