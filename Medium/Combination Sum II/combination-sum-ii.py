#User function Template for python3

class Solution:
    
    def CombinationSum2(self, arr, n, k):
        # code here
        res=[]
        arr.sort()
        
        def dfs(idx,sumi,path):
            if sumi==k:
                res.append(path)
            if sumi>k:
                return 
            for i in range(idx,len(arr)):
                if i>idx and arr[i]==arr[i-1]:
                    continue
                dfs(i+1,sumi+arr[i],path+[arr[i]])
        dfs(0,0,[])
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends