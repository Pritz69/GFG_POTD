#User function Template for python3
class Solution:

	
	def removeDuplicates(self,str):
	    # code here
        d={}
        ans=""
        for x in str :
            if x not in d :
                ans +=x
            d[x]=d.get(x,0)+1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends