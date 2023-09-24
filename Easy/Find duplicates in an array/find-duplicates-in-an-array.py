class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	arr.sort()
    	ans=[]
    	i=1
    	while i < n :
    	    if arr[i]==arr[i-1] :
    	        ans.append(arr[i])
    	        while i<n and arr[i]==arr[i-1] :
    	            i +=1
    	    i +=1
    	if len(ans)==0 :
    	    return [-1]
    	return ans


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends