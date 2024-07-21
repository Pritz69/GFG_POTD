#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        if len(arr)==1 :
            return arr[0]
        mod=10**9+7
        pn=1
        pp=1
        z,p,n=0,0,0
        maxi=float('-inf')
        for x in arr :
            if x < 0 :
                pn=pn*x
                n +=1
                maxi=max(maxi,x)
            elif x >0 :
                pp=pp*x
                p +=1
            else :
                z +=1
        if z==len(arr) :
            return 0
        if n%2==0 :
            return (pn*pp)%mod
        elif n==1 and p==0 :
            return 0
        else :
            return ((pn//maxi)*pp)%mod


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends